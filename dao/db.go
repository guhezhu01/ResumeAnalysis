package dao

import (
	"fmt"
	"github.com/spf13/viper"
	"gorm.io/driver/mysql"
	"gorm.io/gorm"
	"gorm.io/gorm/logger"
	"gorm.io/gorm/schema"
	"log"
	"time"
)

var db *gorm.DB
var err error

func InitDb() {
	dbs := fmt.Sprintf("%s:%s@tcp(%s:%s)/%s?charset=utf8",
		viper.GetString("Mysql.User"),
		viper.GetString("Mysql.Password"),
		viper.GetString("Mysql.Host"),
		viper.GetString("Mysql.Port"),
		viper.GetString("Mysql.Name"),
	)
	db, err = gorm.Open(mysql.Open(dbs), &gorm.Config{
		// gorm日志模式：silent
		Logger: logger.Default.LogMode(logger.Silent),
		// 外键约束
		DisableForeignKeyConstraintWhenMigrating: true,
		// 禁用默认事务（提高运行速度）
		SkipDefaultTransaction: true,
		NamingStrategy: schema.NamingStrategy{
			// 使用单数表名，启用该选项，此时，`User` 的表名应该是 `user`
			SingularTable: true,
		},
	})

	if err != nil {
		log.Fatalln("数据库连接失败:", err)
	}
	sqlDb, _ := db.DB()
	// SetMaxOpenCons 设置数据库的最大连接数量。
	sqlDb.SetMaxOpenConns(10)

	// SetMaxIdleCons 设置连接池中的最大闲置连接数。
	sqlDb.SetMaxIdleConns(10)

	// SetConnMaxLifetime 设置连接的最大可复用时间。
	sqlDb.SetConnMaxLifetime(10 * time.Second)
	log.Println("mysql连接成功")
}
