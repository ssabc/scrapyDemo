// index.js
// 获取应用实例
const app = getApp()
Page({
  data: {
    dataJson: []
  },
  onLoad() {
    if (wx.getUserProfile) {
      this.setData({
        canIUseGetUserProfile: true
      })
    }
    this.getDBData()
  },
  getDBData() {
    wx.request({
      url: 'http://localhost:3000/users',
      data: {},
      header: {
        'content-type': 'application/json' // 默认值
      },
      success: (res) => {
        this.setData({
          dataJson: res.data.data
        })
      }
    })
  }
})
