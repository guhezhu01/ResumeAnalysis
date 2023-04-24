package errMsg

const (
	SUCCESS = 200
	ERROR   = 500
)

var codeMsg = map[uint32]string{
	SUCCESS: "ok",
	ERROR:   "fail",
}

func GetErrMsg(code uint32) string {
	return codeMsg[code]
}
