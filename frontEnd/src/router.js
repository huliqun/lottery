var common = require('commonFunc')
export default function (router) {
  router.map({
    '*': {
      component (resolve) {
        require(['./views/welcome'], resolve)
      }
    },
    '/': {
      component (resolve) {
        require(['./views/login'], resolve)
      }
    },
    '/weixintest': {
      component (resolve) {
        require(['./views/weixintest'], resolve)
      }
    },
    '/login': {
      component (resolve) {
        require(['./views/login'], resolve)
      }
    },
    '/error': {
      component (resolve) {
        require(['./components/errpage'], resolve)
      }
    },
    '/error401': {
      component (resolve) {
        require(['./components/err401'], resolve)
      }
    },
    '/system': {
      component (resolve) {
        require(['./components/mainSystem'], resolve)
      },
      subRoutes: {
        '/home': {
          component (resolve) {
            require(['./views/home'], resolve)
          }
        },
        '/operatorControl': {
          component (resolve) {
            require(['./views/system/operatorControl'], resolve)
          }
        },
        '/groupControl': {
          component (resolve) {
            require(['./views/system/groupControl'], resolve)
          }
        },
        '/menuControl': {
          component (resolve) {
            require(['./views/system/menuControl'], resolve)
          }
        },
        '/groupMenuControl': {
          component (resolve) {
            require(['./views/system/groupMenuControl'], resolve)
          }
        },
        '/printControl': {
          component (resolve) {
            require(['./views/system/printControl'], resolve)
          }
        }
      }
    },
    '/basic': {
      component (resolve) {
        require(['./components/mainSystem'], resolve)
      },
      subRoutes: {
        '/containerYardControl': {
          component (resolve) {
            require(['./views/basic/containerYardControl'], resolve)
          }
        },
        '/carrierControl': {
          component (resolve) {
            require(['./views/basic/carrierControl'], resolve)
          }
        },
        '/carrier2YardControl': {
          component (resolve) {
            require(['./views/basic/carrier2YardControl'], resolve)
          }
        },
        '/shipCoControl': {
          component (resolve) {
            require(['./views/basic/shipCoControl'], resolve)
          }
        },
        '/carrier2ShipCoControl': {
          component (resolve) {
            require(['./views/basic/carrier2ShipCoControl'], resolve)
          }
        }
      }
    },
    '/putBox': {
      component (resolve) {
        require(['./components/mainSystem'], resolve)
      },
      subRoutes: {
        '/putterControl': {
          component (resolve) {
            require(['./views/putBox/putterControl'], resolve)
          }
        },
        '/carManagerInfoControl': {
          component (resolve) {
            require(['./views/putBox/carManagerInfoControl'], resolve)
          }
        },
        '/boxApplyControl': {
          component (resolve) {
            require(['./views/putBox/boxApplyControl'], resolve)
          }
        },
        '/putBoxFixedControl': {
          component (resolve) {
            require(['./views/putBox/putBoxFixedControl'], resolve)
          }
        },
        '/putBoxFinallyControl': {
          component (resolve) {
            require(['./views/putBox/putBoxFinallyControl'], resolve)
          }
        },
        '/carrierParaControl': {
          component (resolve) {
            require(['./views/putBox/carrierParaControl'], resolve)
          }
        },
        '/feeParaControl': {
          component (resolve) {
            require(['./views/putBox/feeParaControl'], resolve)
          }
        },
        '/settleControl': {
          component (resolve) {
            require(['./views/putBox/settleControl'], resolve)
          }
        },
        '/settleQueryControl': {
          component (resolve) {
            require(['./views/putBox/settleQueryControl'], resolve)
          }
        }
      }
    }
  })

  router.beforeEach(({ to, from, next, redirect }) => {
    const toPath = to.path
    const fromPath = from.path
    console.log('to: ' + toPath + ' from: ' + fromPath)
    console.log('to: ' + toPath.replace('.html', ''))
    if (toPath === '/' || toPath === '/login' || toPath === '/error' || toPath === '/error401' || toPath === '/login.html') {
      router.app.isLogin = false
    } else {
      router.app.isLogin = true
    }
    var token = common.getStoreData('token')
    if (typeof (token) !== 'string') {
      if (toPath !== '/login' && toPath !== '/weixintest') {
        redirect('/login')
      }
    }
    next()
  })

  router.afterEach(function ({ to }) {
    console.log(`成功浏览到: ${to.path}`)
  })
}
