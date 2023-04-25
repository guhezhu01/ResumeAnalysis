package routes

import (
	"ResumeAnalysis/handler"
	"github.com/gin-gonic/gin"
)

// InitRoutes 路由接口
func InitRoutes() *gin.Engine {
	engine := gin.Default()
	routes := engine.Group("/api/v1")

	{
		routes.GET("/get/all", handler.GetAllPersonInf)
		routes.DELETE("/delete/:id", handler.DeletePersonInf)

	}

	return engine
}
