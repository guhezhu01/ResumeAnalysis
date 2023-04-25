package config

import (
	"github.com/spf13/viper"
	"log"
	"os"
)

// InitConfig 配置文件初始化
func InitConfig() {
	workDir, _ := os.Getwd()                 //工作目录的路径
	viper.SetConfigName("config")            // 配置文件的文件名
	viper.SetConfigType("yaml")              // 配置文件名的后缀
	viper.AddConfigPath(workDir + "/config") // 获取到配置文件的路径
	err := viper.ReadInConfig()
	if err != nil {
		log.Println("配置文件读取错误！", err)
	}
}
