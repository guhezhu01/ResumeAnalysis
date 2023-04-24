package routes

import (
	"github.com/gin-gonic/gin"
	"net/http"
)

func InitRoutes() *gin.Engine {
	engine := gin.Default()
	engine.GET("/", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{
			"msg": "ok",
		})
	})
	return engine
}
