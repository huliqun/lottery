/**
 * Created by  on 2016/4/1.
 */
import {
    SET_ERROR
}  from '../mutation-types'

const state  = {
		errCode: "",
		errMsg: ""
}

// mutations
const mutations = {
    [SET_ERROR] (state, errCode, errMsg) {
        state.errCode = errCode
        state.errMsg = errMsg
    }
}

export default {
    state,
    mutations
}
