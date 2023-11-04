from bs4 import BeautifulSoup
import requests
import json

import pandas as pd

headers = {
    'accept': '*/*',
    'accept-encoding': 'gzip',
    'accept-language': 'en-US,en;q=0.9',
    'referer': 'https://www.google.com',
    'cookie': 'wsjregion=na%2Cus; dnsDisplayed=undefined; signedLspa=undefined; cX_P=lo8u0i6qlzvf2n7g; _rdt_uuid=1698424363842.22b10e0c-70a0-47b1-9390-63ea1f781da5; _ncg_domain_id_=5d1f2fa3-7b44-44bc-ae67-4baba2cea0ed.1.1698424363891.1761496363891; cX_G=cx%3A89k831np2t2i1pkrej0regh0k%3A37cvnxn23i0if; _dj_sp_id=cbff54af-18df-41c0-bb68-319fce9f18cd; _pin_unauth=dWlkPU5EQmxZbVJoWkdJdE4yTmhNaTAwWWpsakxXRXhZalF0TW1Vd1pXWmxNbVk1TUdVeQ; djcs_route=0ac591cf-5812-4060-99e2-279b26712da9; TR=V2-855f5552f14d238a00014923466ba0fbd99ecc9188a876469b111b2436fa6ac5; ab_uuid=5834b63f-744b-461c-8c99-eb83d68dac5f; optimizelyEndUserId=oeu1698424513931r0.7937193913142717; _ncg_id_=5d1f2fa3-7b44-44bc-ae67-4baba2cea0ed; _ncg_g_id_=f30e53ce-dedc-411f-af91-7b100b1d5896.3.1698425307.1761496363891; _ga_T1HSMPG165=GS1.1.1698424516.1.1.1698425403.0.0.0; _ga_2EFCPNJ1HR=GS1.1.1698425263.1.1.1698425403.0.0.0; _lr_env_src_ats=false; ccpaUUID=908cf665-fb50-4cef-b040-90809ea43d8f; consentUUID=7ba53be9-4d40-4ee3-b453-1f7d2b547b4b; _cls_v=c54c395a-2a6f-4439-aa60-a8be306a1a4d; DJSESSION=country%3Dus%7C%7Ccontinent%3Dna%7C%7Cregion%3Dla; gdprApplies=false; ccpaApplies=false; vcdpaApplies=false; regulationApplies=gdpr%3Afalse%2Ccpra%3Afalse%2Cvcdpa%3Afalse; _pubcid=8a651303-d230-4669-b4af-7ac7beafa19f; AMCVS_CB68E4BA55144CAA0A4C98A5%40AdobeOrg=1; AMCV_CB68E4BA55144CAA0A4C98A5%40AdobeOrg=1585540135%7CMCIDTS%7C19666%7CMCMID%7C05180357462714851243822272933240899147%7CMCAAMLH-1699726985%7C7%7CMCAAMB-1699726985%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1699129385s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.4.0; s_cc=true; _cls_s=45df889e-2aa8-4679-9688-eabe267369db:1; _pxvid=ac1fd138-7b43-11ee-ae8a-cc595c3718f9; s_vnum=1729970811737%26vn%3D3; s_vmonthnum=1701410400791%26vn%3D1; s_sq=djwsj%3D%2526c.%2526a.%2526activitymap.%2526page%253DDWSJN_Commerce_CAJ_Thank_You%2526link%253DNO%25252C%252520THANKS%2526region%253Dcard_order_success%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253DDWSJN_Commerce_CAJ_Thank_You%2526pidt%253D1%2526oid%253Dfunctionsn%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DBUTTON; _scid=9a9cd14a-98f2-45a9-9932-51574e97cff1; _pcid=%7B%22browserId%22%3A%22lo8u0i6qlzvf2n7g%22%7D; ca_rt=aTAjwzwGdhFBR60ZuB0fkQ.xLPcvm8N79TaZUd7z0WMDtodb_aZxnP3rZy9C2Nt0oWxp7XCRk8rs-4byduudlnziASnVwgiF8BzgtP7JNVJ9_t2dIPVCyiuiMcm3IxJWyY; ca_id=eJw9kMtOwzAQRf_F66SNHduJuyJVAgoqbVUKLBCKJrbTmjxaNS4BIf4d9wG7uefeGc3MN9qYD90VHbQaTdAcStMhD1XQmubrjy6hrsFR3YJpnN5D3UHXx-JmcyIjuWudezwa5UytgUSRDHwelNKnTEW-4Jz4lY4CTCNFmApc2h5A1ueGmLGKMUYqTBUJYwgClxMkpJyXEFSlEkJLKXAcQxxxykWJMS4JDXkFHCRzww67Rvdo8opuV1m2yu78fJ7mz3n6lMyc-_J47-fLJL2WyTxdLfK0WCfTWba-wofFNJ9lF4HePARHuy2sOZ2PuRCYUBqGHpIHDVarAuyZxxQzwSMPmSv4D-rP_QUwxs_A9G5BtLV230_G42EYRkP_fvrcWDZGdxb9_AKzanCe.mooqExvp7KYrrgtDQJjGtB1r7JVpcRN45P-YXSD3vnYx_RTZAvnD7xXBJJenw3EM77zRGeG-Ku_nJGScxGdYNFhHS2foS4itQxDp2-HMHmfzsnHEX1gtYZhZasw5KPwwQW11OW_vSnEWnI9wJPiVCMqTNU0CbOHScHWL8lFofSxQx7kxDeRnpmETIBh4aEL65KgaDnvqAXhdjV5sdNPoOFjRqsB-N0EDHBhJKBx4AteXTRbO-ehYrDGUBSNyoXzhwbL6075fNtHKOYGSyAKvWx00pQn0MhjicUlKvdY1Z_ogC4Qx1htHxqlfJOkN3-jSdXwjJdSlDqKeqwlOS1QC5_qYZJKD8gfAPNch5tSJJHnabM85dI_nhsYsYr0hY8pAfuQiIYRnamZKVwZ1t_f39VSLlTosbRT-LskEuds0B-HuEy4tTE5XS-QI4zw7HOnc740xKI-YefniJoTBCFytYyIR8nZhF4KPER8SVzbJSMYQ3sLgFM0AAmzWbmk1LlH0qKXGq-fljAJi6udeIMehMo4ja-n31dHGJMjKBw5-vOmMQDNRFQxtGxcxcqPf2m6HCsvlO9e7pin9QNb_s11LMqjCMa9B6j5wUYly3Ce7Eql6eEiM9TqiKq4NR15genaKfrlrI7Et7iNxxNS5pRLLbCNjUXdsLWWKycqV17XO0Rw; usr_prof_v2=eyJhIjp7InNiIjoiRnJlZSBSZWcifSwib3AiOnsiaSI6IjQ1NGU4NDAwIiwiaiI6eyJqdCI6Im5hIiwiamYiOiJzIiwiamkiOiJlIn19LCJpYyI6Nn0%3D; utag_main=v_id:018b71fb19b90022014739ac335005075005406d009de$_sn:3$_se:7$_ss:0$_st:1699126237968$vapi_domain:wsj.com$ses_id:1699122185297%3Bexp-session$_pn:12%3Bexp-session$_prevpage:WSJ_Article_Markets_A%20Couple%20Paid%20Down%20Most%20of%20Their%20Debt.%20Now%20They%20Need%20a%20New%20Financial%20Plan.%3Bexp-1699128037975; _pctx=%7Bu%7DN4IgrgzgpgThIC5QA4CsqBm7UCYMEYAWAExwGZkBDABlqIE5zCA2ZgIxozePvqgGN%2B9fMirIA7Mxb02%2BOWxyEyzDJWaV%2BqRKAAOMKBgCWAD0QgA7hABWIADQgALgE8dUMwGEAGiAC%2BP%2B5CwAMoOlA6QZpQAdgD2UXYgEIYOUACSxGaMOOQizPgUuITIzPS0vkA; s_tp=8844; s_ppv=WSJ_Article_Markets_A%2520Couple%2520Paid%2520Down%2520Most%2520of%2520Their%2520Debt.%2520Now%2520They%2520Need%2520a%2520New%2520Financial%2520Plan.%2C11%2C11%2C1003; _scid_r=9a9cd14a-98f2-45a9-9932-51574e97cff1; _uetsid=328f3b307b3f11ee8ba367cc6e787cbb; _uetvid=746e776074e611ee97c14f8866299e40; _ncg_sp_ses.5378=*; _dj_ses.9183=*; _dj_id.9183=.1699122186.7.1699124439.1699124420.3826df51-9879-4e60-91e8-703ce7765398; _gcl_au=1.1.1796083592.1699124439; _ncg_sp_id.5378=5d1f2fa3-7b44-44bc-ae67-4baba2cea0ed.1698424364.18.1699124439.1699124420.b559a6f9-c422-4e11-b2ad-e59591e8e494.9a736f5e-013c-4099-a356-7c8c8787bdf3.32d9f8f8-5ad9-449d-9773-cfff36f86540.1699124439014.1; _sctr=1%7C1699074000000; dicbo_id=%7B%22dicbo_fetch%22%3A1699124439210%7D',
    'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjY2ZDZkNmZlLTRmN2UtNGQxYy05ZmQzLTA2MTg1N2VkZDVlOSJ9.eyJnaXZlbl9uYW1lIjoiTmFiaW4iLCJmYW1pbHlfbmFtZSI6IlBha2thIiwiZW1haWwiOiJwYWtuYW5zODlAZ21haWwuY29tIiwidXVpZCI6ImVlYTI3N2MwLTYwYmMtNDVkNy05NjYyLWZlNzAxNDdkMjVkMCIsInRyYWNraWQiOiI4NTVmNTU1MmYxNGQyMzhhMDAwMTQ5MjM0NjZiYTBmYmQ5OWVjYzkxODhhODc2NDY5YjExMWIyNDM2ZmE2YWM1Iiwicm9sZXMiOlsiRlJFRVJFRy1JTkRJVklEVUFMIiwiV1NKLUlQQUQiLCJXU0otQU5EUk9JRF9UQUJMRVQiLCJXU0otTU9CSUxFIiwiV1NKIl0sImF1dGhfdGltZSI6MTY5OTEyNDQzMywiY3JlYXRlZF9hdCI6MTY5ODQxNTk2NywiaWF0IjoxNjk5MTI0NDMzLCJleHAiOjE2OTk1NTY0MzMsImlzcyI6Imh0dHBzOi8vd3d3Lndzai5jb20vY2xpZW50In0.mooqExvp7KYrrgtDQJjGtB1r7JVpcRN45P-YXSD3vnYx_RTZAvnD7xXBJJenw3EM77zRGeG-Ku_nJGScxGdYNFhHS2foS4itQxDp2-HMHmfzsnHEX1gtYZhZasw5KPwwQW11OW_vSnEWnI9wJPiVCMqTNU0CbOHScHWL8lFofSxQx7kxDeRnpmETIBh4aEL65KgaDnvqAXhdjV5sdNPoOFjRqsB-N0EDHBhJKBx4AteXTRbO-ehYrDGUBSNyoXzhwbL6075fNtHKOYGSyAKvWx00pQn0MhjicUlKvdY1Z_ogC4Qx1htHxqlfJOkN3-jSdXwjJdSlDqKeqwlOS1QC5_qYZJKD8gfAPNch5tSJJHnabM85dI_nhsYsYr0hY8pAfuQiIYRnamZKVwZ1t_f39VSLlTosbRT-LskEuds0B-HuEy4tTE5XS-QI4zw7HOnc740xKI-YefniJoTBCFytYyIR8nZhF4KPER8SVzbJSMYQ3sLgFM0AAmzWbmk1LlH0qKXGq-fljAJi6udeIMehMo4ja-n31dHGJMjKBw5-vOmMQDNRFQxtGxcxcqPf2m6HCsvlO9e7pin9QNb_s11LMqjCMa9B6j5wUYly3Ce7Eql6eEiM9TqiKq4NR15genaKfrlrI7Et7iNxxNS5pRLLbCNjUXdsLWWKycqV17XO0Rw',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}
template = 'https://www.cnn.com/{}'
import time


def get_beautified_response(url):
    response = requests.get(url, headers=headers)
    return BeautifulSoup(response.text, 'lxml')

def get_body_from_individual_page(url):

    try:
        response = get_beautified_response(url)
        article = response.find("article", "css-15rv4ep")
        section = article.find("section", "ef4qpkp0")
        
        paragraphs = section.find_all("p", {"class":"css-k3zb6l-Paragraph"}, recursive=True)



        body = ""
        for paragraph in paragraphs:
            body += paragraph.text.strip("\n") if paragraph is not None else "" + "\n"

        return body
    except Exception as e:
        print("An error has occurred: ", e)

if __name__ == '__main__':
    file_name = "wsj.json"
    url = "https://www.wsj.com/personal-finance/savings/-couple-paid-down-debt-new-financial-plan-d0aaba18"

    body = get_body_from_individual_page(url)
    print(body)

    # data = pd.read_json(file_name, lines=True)
    #
    # for index, row in data.iterrows():
    #     url = row.get("url")
    #
    #     body = get_body_from_individual_page(url)
    #     data.at[index, "body"] = body



