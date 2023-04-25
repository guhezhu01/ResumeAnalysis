package errMsg

// 自定义错误处理

const (
	SUCCESS            = 200
	ERROR              = 500
	GET_PERSON_FAIL    = 10001
	DELETE_PERSON_FAIL = 10002
)

var codeMsg = map[uint32]string{
	SUCCESS:            "ok",
	ERROR:              "fail",
	GET_PERSON_FAIL:    "获取所有简历失败",
	DELETE_PERSON_FAIL: "简历删除失败",
}

func GetErrMsg(code uint32) string {
	return codeMsg[code]
}
