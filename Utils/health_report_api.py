import datetime
import json
import Utils.timeUtil as timeUtil
from .login import login_xmuxg


def health_report(USERNAME, PASSWORD, N):
    Headers = {'content-type': 'application/json'}
    s = login_xmuxg(USERNAME, PASSWORD)
    if not s:
        return 'Failed to Cores. Please check username and password. '
    try:
        resp = s.get('https://xmuxg.xmu.edu.cn/api/app/214/business/now?getFirst=true')  # 新增getFirst参数，避免加载太久
        form_dict = resp.json()
        # change deate in below line ()
        for i in range(N):
            businessId = form_dict['data'][i]['business']['id']
            resp = s.get(f'https://xmuxg.xmu.edu.cn/api/formEngine/business/{businessId}/myFormInstance')
            myFormJson = resp.json()
            formid = myFormJson['data']['id']
            form_url = f'https://xmuxg.xmu.edu.cn/api/formEngine/formInstance/{formid}'
            false = 'false'
            true = 'true'
            form_data = {"formData": [
                {"name": "select_1582538796361", "title": "今日体温 Body temperature today （℃）",
                 "value": {"stringValue": "37.3以下 Below 37.3 degree celsius"}, "hide": false},
                {"name": "select_1582538846920",
                 "title": "是否出现发热或咳嗽或胸闷或呼吸困难等症状？Do you have sypmtoms such as fever, coughing, chest tightness or breath difficulties?",
                 "value": {"stringValue": "否 No"}, "hide": false},
                {"name": "select_1582538939790",
                 "title": "Can you hereby declare that all the information provided is all true and accurate and there is no concealment, false information or omission. 本人是否承诺所填报的全部内容均属实、准确，不存在任何隐瞒和不实的情况，更无遗漏之处。",
                 "value": {"stringValue": "是 Yes"}, "hide": false},
                {"name": "input_1582538924486", "title": "备注 Notes", "value": {"stringValue": ""},
                 "hide": false},
                {"name": "datetime_1611146487222", "title": "打卡时间（无需填写，保存后会自动更新）",
                 "value": {"dateValue": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}, "hide": false,
                 "readonly": false},
                {"name": "select_1584240106785", "title": "学生本人是否填写",
                 "value": {"stringValue": "是"}, "hide": false, "readonly": false}
            ], "playerId": "owner"}
            resp = s.post(form_url, data=json.dumps(form_data), headers=Headers)
            # print(resp.content.decode('utf-8'))
        # print(resp.content.decode('utf-8'))
        print(timeUtil.get_current_time()+ '打卡完毕!')
        return 'Succeeded'
    except Exception as e:
        print(e)
        return 'Exception!'
