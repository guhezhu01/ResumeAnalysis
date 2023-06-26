package routes

import (
	"ResumeAnalysis/handler"
	"ResumeAnalysis/middlerware"
	"github.com/gin-gonic/gin"
)

// InitRoutes 路由接口
func InitRoutes() *gin.Engine {
	engine := gin.Default()

	routes := engine.Group("/api/v1")
	routes.Use(middlerware.Cors())
	{
		routes.GET("/get/all", handler.GetAllPersonInf)
		routes.DELETE("/delete/:id", handler.DeletePersonInf)

	}

	return engine
}
