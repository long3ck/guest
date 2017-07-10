#coding=utf-8
__author__ = 'Chenkun'
__date__ = '2017/06/19 17:26'

import unittest
import requests

class GetEventListTest(unittest.TestCase):
    ''' 查询发布会信息（带用户认证） '''
    def setUp(self):
        self.base_url = "http://127.0.0.1:8000/api/sec_get_event_list/"
        self.auth_user = ('long3ck', 'mymxV8sGdzs')


    def test_1_get_event_list_auth_null(self):
        ''' auth 为空 '''
        r = requests.get(self.base_url, params={'eid':''})
        result1 = r.json()
        print u'auth 为空场景,结果：',result1
        self.assertEqual(result1['status'], 10011)
        self.assertEqual(result1['message'], 'user auth null')


    def test_2_get_event_list_auth_error(self):
        ''' auth 错误 '''
        r = requests.get(self.base_url, auth=('long3ck','123'), params={'eid':''})
        result2 = r.json()
        print u'auth 错误场景,结果：',result2
        self.assertEqual(result2['status'], 10012)
        self.assertEqual(result2['message'], 'user auth fail')


    def test_3_get_event_list_eid_null(self):
        ''' eid 参数为空 '''
        r = requests.get(self.base_url, auth=self.auth_user, params={'eid':''})
        result3 = r.json()
        print u'eid 参数为空场景,结果：',result3
        self.assertEqual(result3['status'], 10021)
        self.assertEqual(result3['message'], 'parameter error')


    def test_4_get_event_list_eid_success(self):
        ''' 根据 eid 查询结果成功 '''
        r = requests.get(self.base_url, auth=self.auth_user, params={'eid':1})
        result4 = r.json()
        print u'根据 eid 查询结果成功场景,结果：',result4
        self.assertEqual(result4['status'], 200)
        self.assertEqual(result4['message'], 'success')
        self.assertEqual(result4['data']['name'],u'mx6 发布会')
        self.assertEqual(result4['data']['address'],u'北京国家会议中心')
        self.assertEqual(result4['data']['start_time'], "2016-10-15T18:00:00")


if __name__ == '__main__':
    unittest.main()