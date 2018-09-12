import session from '@/app/mirari/api/session';
import qs from  'qs';

export default {
    set_sellpoint() {
        return session.post('SV/api/SetSellpointApiView/SV/get/EmployeeAccess/');
    },
};
    