package main

import (
	"ResumeAnalysis/config"
	"ResumeAnalysis/dao"
	"ResumeAnalysis/routes"
	"github.com/spf13/viper"
	"log"
	"os"
	"os/signal"
	"syscall"
)

func main() {
	config.InitConfig() // 初始化配置文件
	dao.InitDb()
	engine := routes.InitRoutes()
	// 启用协程
	go func() {
		if err := engine.Run(viper.GetString("HttpPort")); err != nil {
			return
		}
	}()

	// 管道监听到协程退出，则运行结束
	quit := make(chan os.Signal)
	signal.Notify(quit, syscall.SIGINT, syscall.SIGINT)
	<-quit
	log.Println("关闭服务！")
}
