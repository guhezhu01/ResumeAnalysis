package handler

import (
	"ResumeAnalysis/dao"
	"ResumeAnalysis/utils/errMsg"
	"github.com/gin-gonic/gin"
	"net/http"
	"strconv"
)

// GetAllPersonInf 获取所有简历信息
func GetAllPersonInf(c *gin.Context) {
	data, total, code := dao.GetAllPersonInf()
	c.JSON(http.StatusOK, gin.H{
		"code":  code,
		"msg":   errMsg.GetErrMsg(code),
		"data":  data,
		"total": total,
	})
}

// DeletePersonInf 删除简历
func DeletePersonInf(c *gin.Context) {
	// ParseUint将字符串转成uint64
	id, _ := strconv.ParseUint(c.Param("id"), 10, 32)

	code := dao.DeletePersonInf(id)
	c.JSON(http.StatusOK, gin.H{
		"code": code,
		"msg":  errMsg.GetErrMsg(code),
	})

}
