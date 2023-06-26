package dao

import (
	"ResumeAnalysis/utils/errMsg"
	"errors"
	"gorm.io/gorm"
	"log"
)

type PersonInformation struct {
	Id        uint64 `gorm:"type:int;not null" json:"id"`
	Name      string `gorm:"type:varchar(10);not null" json:"name"`
	Age       uint32 `gorm:"type:int(4);not null" json:"age"`
	Education string `gorm:"type:varchar(10);" json:"education"`
	School    string `gorm:"type:varchar(20);" json:"school"`
	WorkAge   uint32 `gorm:"type:int(4);" json:"work_age"`
	Introduce string `gorm:"type:varchar(255);" json:"introduce"`
}

// GetAllPersonInf 从mysql获取所有简历信息
func GetAllPersonInf() ([]PersonInformation, int64, uint32) {
	var data []PersonInformation
	var total int64
	err := db.Model(&data).Find(&data).Count(&total).Error
	if err != nil {
		log.Fatalln("获取所有简历信息失败！,", err)
		return nil, 0, errMsg.GET_PERSON_FAIL
	}
	return data, total, errMsg.SUCCESS
}

// DeletePersonInf 从mysql删除简历
func DeletePersonInf(id uint64) uint32 {
	err := db.Where("id =?", id).Delete(PersonInformation{}).Error
	if err != nil {
		log.Fatalln("简历删除失败！,", err)
		return errMsg.DELETE_PERSON_FAIL
	}

	return errMsg.SUCCESS
}

func (personInformation *PersonInformation) BeforeDelete(tx *gorm.DB) (err error) {
	db.Model(personInformation).Where("id=?", personInformation.Id)
	if personInformation.Name == "管理员" {
		return errors.New("管理员账户不能删除")
	}
	return
}
