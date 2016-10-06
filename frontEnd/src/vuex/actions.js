import * as types from './mutation-types'

// 设置错误
export const setError = ({ dispatch }, errCode, errMsg) => {
    dispatch(types.SET_ERROR, errCode, errMsg)
}
