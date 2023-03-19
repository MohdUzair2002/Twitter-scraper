import requests
import csv
import json
names=[]
list1=[]
indicator=[]
def find_entries(json_obj):
    # Base case: object is a dictionary and contains "entries" key
    if isinstance(json_obj, dict) and "entries" in json_obj:
        return json_obj["entries"]
    
    # Recursive case: object is a dictionary or a list of dictionaries
    if isinstance(json_obj, dict):
        for key in json_obj:
            result = find_entries(json_obj[key])
            if result:
                return result
    elif isinstance(json_obj, list):
        for item in json_obj:
            result = find_entries(item)
            if result:
                return result
    
    # Key not found
    return None
def find_entry(json_obj, index):
    # Base case: object is a dictionary and contains "entries" key
    if isinstance(json_obj, dict) and "entries" in json_obj:
        try:
            return json_obj["entries"][index]
        except IndexError:
            return None
    
    # Recursive case: object is a dictionary or a list of dictionaries
    if isinstance(json_obj, dict):
        for key in json_obj:
            result = find_entry(json_obj[key], index)
            if result:
                return result
    elif isinstance(json_obj, list):
        for item in json_obj:
            result = find_entry(item, index)
            if result:
                return result
    
    # Key not found
    return None

cookies = {
    'guest_id_marketing': 'v1%3A167735099795215138',
    'guest_id_ads': 'v1%3A167735099795215138',
    'guest_id': 'v1%3A167735099795215138',
    '_ga': 'GA1.2.1051661728.1677431895',
    'kdt': 'sctps27O2wo1cH3NZiZyweqqofnBAi09XkbMT5ll',
    'auth_token': 'e2d8475825085d5b747d98d50d251e5e1f48ce8e',
    'ct0': '4d71a722fd1b1bebed116022cda884499f9d8769187440b228bb97d2b7cc63d607bc954776ecec9fd9b1e0b98b7d6313e3df5e2075e34a86a1f4aa3642be4c0dbfccfbce46b19218d4aaa39badc16e48',
    'twid': 'u%3D1583859324920758273',
    '_gid': 'GA1.2.381662334.1677683489',
    'personalization_id': '"v1_NxIjznjJEAlTQROFKIErVg=="',
}

headers = {
    'authority': 'api.twitter.com',
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    'content-type': 'application/json',
    # 'cookie': 'guest_id_marketing=v1%3A167735099795215138; guest_id_ads=v1%3A167735099795215138; guest_id=v1%3A167735099795215138; _ga=GA1.2.1051661728.1677431895; kdt=sctps27O2wo1cH3NZiZyweqqofnBAi09XkbMT5ll; auth_token=e2d8475825085d5b747d98d50d251e5e1f48ce8e; ct0=4d71a722fd1b1bebed116022cda884499f9d8769187440b228bb97d2b7cc63d607bc954776ecec9fd9b1e0b98b7d6313e3df5e2075e34a86a1f4aa3642be4c0dbfccfbce46b19218d4aaa39badc16e48; twid=u%3D1583859324920758273; _gid=GA1.2.381662334.1677683489; personalization_id="v1_NxIjznjJEAlTQROFKIErVg=="',
    'origin': 'https://twitter.com',
    'referer': 'https://twitter.com/',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'x-csrf-token': '4d71a722fd1b1bebed116022cda884499f9d8769187440b228bb97d2b7cc63d607bc954776ecec9fd9b1e0b98b7d6313e3df5e2075e34a86a1f4aa3642be4c0dbfccfbce46b19218d4aaa39badc16e48',
    'x-twitter-active-user': 'yes',
    'x-twitter-auth-type': 'OAuth2Session',
    'x-twitter-client-language': 'en',
}
# cursor="1759264665080628096|1631301755801173776"
cursor="1757435318228792446|1631301755801170115"
j=0
count=1000

params = {
    
    'variables': '{"userId":"714552914","count":100,"includePromotedContent":false,"withSuperFollowsUserFields":true,"withDownvotePerspective":false,"withReactionsMetadata":false,"withReactionsPerspective":false,"withSuperFollowsTweetFields":true}',
        'features': '{"responsive_web_twitter_blue_verified_badge_is_enabled":true,"responsive_web_graphql_exclude_directive_enabled":false,"verified_phone_label_enabled":false,"responsive_web_graphql_timeline_navigation_enabled":true,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"tweetypie_unmention_optimization_enabled":true,"vibe_api_enabled":true,"responsive_web_edit_tweet_api_enabled":true,"graphql_is_translatable_rweb_tweet_is_translatable_enabled":true,"view_counts_everywhere_api_enabled":true,"longform_notetweets_consumption_enabled":true,"tweet_awards_web_tipping_enabled":false,"freedom_of_speech_not_reach_fetch_enabled":false,"standardized_nudges_misinfo":true,"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled":false,"interactive_text_enabled":true,"responsive_web_text_conversations_enabled":false,"longform_notetweets_richtext_consumption_enabled":false,"responsive_web_enhance_cards_enabled":false}',
    }
while(j<count):
    

    response = requests.get(
        'https://api.twitter.com/graphql/utPIvA97eaEvxfra_PQz_A/Followers',
        params=params,
        cookies=cookies,
        headers=headers,
    )

    # data=response.json()
    # with open('data.txt','w',encoding='utf-8') as f:
    #    f.write(str(data))
    # try:
    print(response.json())
    with open('response.txt','w',encoding='utf-8') as f:
        f.write(response.text)
    #  if (len(response.json())==0):
    #      break
    # except:
    #     break
    # json_obj = json.loads(response.text)

    #     # Find "entries" key
    # entries1 = find_entry(json_obj)
    for i in range(100):
        print(i)
        # try:
        json_obj = json.loads(response.text)
        entries=find_entry(json_obj,i)
        try:
         data_json=entries['content']['itemContent']['user_results']['result']['legacy']['name']
        except KeyError :
            break
        # except:
        #     print("gg")
        #     indicator.append(1)
        #     break
        print(data_json)
        names.append(data_json)
            # print(response.json())
            # list1.append(response.json())
        # except:
        #      pass
    if 1 in indicator:
        break
    json_obj = json.loads(response.text)

        # Find "entries" key
    entries1 = find_entries(json_obj)
    cursor=entries1[-2]['content']['value']
    break_indic=str(cursor).split("|")[0]
    print(break_indic)
    if break_indic =='-1'or break_indic=='0':
        break
    params = {
    
    'variables': '{"userId":"714552914","count":100,"cursor":"%s","includePromotedContent":false,"withSuperFollowsUserFields":true,"withDownvotePerspective":false,"withReactionsMetadata":false,"withReactionsPerspective":false,"withSuperFollowsTweetFields":true}'%cursor,
    'features': '{"responsive_web_twitter_blue_verified_badge_is_enabled":true,"responsive_web_graphql_exclude_directive_enabled":false,"verified_phone_label_enabled":false,"responsive_web_graphql_timeline_navigation_enabled":true,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"tweetypie_unmention_optimization_enabled":true,"vibe_api_enabled":true,"responsive_web_edit_tweet_api_enabled":true,"graphql_is_translatable_rweb_tweet_is_translatable_enabled":true,"view_counts_everywhere_api_enabled":true,"longform_notetweets_consumption_enabled":true,"tweet_awards_web_tipping_enabled":false,"freedom_of_speech_not_reach_fetch_enabled":false,"standardized_nudges_misinfo":true,"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled":false,"interactive_text_enabled":true,"responsive_web_text_conversations_enabled":false,"longform_notetweets_richtext_consumption_enabled":false,"responsive_web_enhance_cards_enabled":false}',
    }
    # with open('data2.csv','w',encoding='utf-8') as file:
    #     file.write(str(dat))

    print(cursor)
    list1.append(cursor)

    # print(data_json)
    j+=1
with open('data5.txt','w',encoding='utf-8') as file:
        writer=csv.writer(file)
        writer.writerows(names)
with open('data23.txt','w',encoding='utf-8') as file:
     writer=csv.writer(file)
     writer.writerows(list1)

print(len(names))
