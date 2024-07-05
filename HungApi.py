import http.client
import json

# headers = {
#   'accept': '*/*',
#   'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
#   'authorization': 'Bearer search-1frxia53o7tb6m2h14kphs1e',
#   'content-type': 'application/json',
#   'origin': 'https://eduquiz.vn',
#   'priority': 'u=1, i',
#   'referer': 'https://eduquiz.vn/',
#   'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
#   'sec-ch-ua-mobile': '?1',
#   'sec-ch-ua-platform': '"Android"',
#   'sec-fetch-dest': 'empty',
#   'sec-fetch-mode': 'cors',
#   'sec-fetch-site': 'cross-site',
#   'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36',
#   'x-elastic-client-meta': 'ent=8.9.0-legacy,js=browser,t=8.9.0-legacy,ft=universal',
#   'x-swiftype-client': 'elastic-app-search-javascript',
#   'x-swiftype-client-version': '8.9.0'
# }
# conn.request("POST", "/api/as/v1/engines/exams-prod/search.json", payload, headers)
# res = conn.getresponse()
# data = res.read()
# print(data.decode("utf-8"))
# res = json.loads(data.decode("utf-8"))
# schools = res['facets']['schools'][0]['data']
# filtered_schools = [school['value'] for school in schools if 'Y' in school['value']]
# print(filtered_schools)

def get_exams(school_name):
    conn = http.client.HTTPSConnection("eduquiz-01.ent.us-central1.gcp.cloud.es.io")
    payload = json.dumps({
      "query": "",
      "facets": {
        "year": {
          "type": "value",
          "size": 100
        },
        "level_schools": {
          "type": "value",
          "size": 100
        },
        "schools": {
          "type": "value",
          "size": 100
        },
        "skills": {
          "type": "value",
          "size": 100
        },
        "subjects": {
          "type": "value",
          "size": 100
        },
        "majors": {
          "type": "value",
          "size": 100
        },
        "topics": {
          "type": "value",
          "size": 100
        }
      },
      "filters": {
        "all": [
          {
            "all": [
              {
                "schools": school_name
              }
            ]
          }
        ]
      },
      "result_fields": {
        "code": {
          "raw": {},
          "snippet": {
            "size": 100,
            "fallback": True
          }
        },
        "chanel_id": {
          "raw": {},
          "snippet": {
            "size": 100,
            "fallback": True
          }
        },
        "favorites_count": {
          "raw": {},
          "snippet": {
            "size": 100,
            "fallback": True
          }
        },
        "description": {
          "raw": {},
          "snippet": {
            "size": 100,
            "fallback": True
          }
        },
        "deleted_by": {
          "raw": {},
          "snippet": {
            "size": 100,
            "fallback": True
          }
        },
        "created_at": {
          "raw": {},
          "snippet": {
            "size": 100,
            "fallback": True
          }
        },
        "ratings_avg_rating": {
          "raw": {},
          "snippet": {
            "size": 100,
            "fallback": True
          }
        },
        "type": {
          "raw": {},
          "snippet": {
            "size": 100,
            "fallback": True
          }
        },
        "thumbnail_url": {
          "raw": {},
          "snippet": {
            "size": 100,
            "fallback": True
          }
        },
        "is_question_shuffle": {
          "raw": {},
          "snippet": {
            "size": 100,
            "fallback": True
          }
        },
        "likers_count": {
          "raw": {},
          "snippet": {
            "size": 100,
            "fallback": True
          }
        },
        "skills": {
          "raw": {},
          "snippet": {
            "size": 100,
            "fallback": True
          }
        },
        "download": {
          "raw": {},
          "snippet": {
            "size": 100,
            "fallback": True
          }
        },
        "majors": {
          "raw": {},
          "snippet": {
            "size": 100,
            "fallback": True
          }
        },
        "updated_at": {
          "raw": {},
          "snippet": {
            "size": 100,
            "fallback": True
          }
        },
        "bizapp": {
          "raw": {},
          "snippet": {
            "size": 100,
            "fallback": True
          }
        },
        "viewed": {
          "raw": {},
          "snippet": {
            "size": 100,
            "fallback": True
          }
        },
        "alias": {
          "raw": {},
          "snippet": {
            "size": 100,
            "fallback": True
          }
        },
        "total_question": {
          "raw": {},
          "snippet": {
            "size": 100,
            "fallback": True
          }
        },
        "keyword": {
          "raw": {},
          "snippet": {
            "size": 100,
            "fallback": True
          }
        },
        "topics": {
          "raw": {},
          "snippet": {
            "size": 100,
            "fallback": True
          }
        },
        "subjects": {
          "raw": {},
          "snippet": {
            "size": 100,
            "fallback": True
          }
        },
        "created_by": {
          "raw": {},
          "snippet": {
            "size": 100,
            "fallback": True
          }
        },
        "deleted_at": {
          "raw": {},
          "snippet": {
            "size": 100,
            "fallback": True
          }
        },
        "version": {
          "raw": {},
          "snippet": {
            "size": 100,
            "fallback": True
          }
        },
        "chanel": {
          "raw": {},
          "snippet": {
            "size": 100,
            "fallback": True
          }
        },
        "is_answer_shuffle": {
          "raw": {},
          "snippet": {
            "size": 100,
            "fallback": True
          }
        },
        "schools": {
          "raw": {},
          "snippet": {
            "size": 100,
            "fallback": True
          }
        },
        "name": {
          "raw": {},
          "snippet": {
            "size": 100,
            "fallback": True
          }
        },
        "updated_by": {
          "raw": {},
          "snippet": {
            "size": 100,
            "fallback": True
          }
        },
        "exam_url": {
          "raw": {},
          "snippet": {
            "size": 100,
            "fallback": True
          }
        },
        "custom_data": {
          "raw": {},
          "snippet": {
            "size": 100,
            "fallback": True
          }
        },
        "level_schools": {
          "raw": {},
          "snippet": {
            "size": 100,
            "fallback": True
          }
        },
        "status": {
          "raw": {},
          "snippet": {
            "size": 100,
            "fallback": True
          }
        },
        "id": {
          "raw": {},
          "snippet": {
            "size": 100,
            "fallback": True
          }
        }
      },
      "search_fields": {
        "name": {},
        "alias": {},
        "description": {},
        "keyword": {}
      },
      "sort": {
        "created_at": "desc"
      },
      "page": {
        "size": 20,
        "current": 1
      }
    })
    headers = {
      'accept': '*/*',
      'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
      'authorization': 'Bearer search-1frxia53o7tb6m2h14kphs1e',
      'content-type': 'application/json',
      'origin': 'https://eduquiz.vn',
      'priority': 'u=1, i',
      'referer': 'https://eduquiz.vn/',
      'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
      'sec-ch-ua-mobile': '?1',
      'sec-ch-ua-platform': '"Android"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'cross-site',
      'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36',
      'x-elastic-client-meta': 'ent=8.9.0-legacy,js=browser,t=8.9.0-legacy,ft=universal',
      'x-swiftype-client': 'elastic-app-search-javascript',
      'x-swiftype-client-version': '8.9.0'
    }
    conn.request("POST", "/api/as/v1/engines/exams-prod/search.json", payload, headers)
    res = conn.getresponse()
    data = res.read()
    quiz = json.loads(data.decode("utf-8"))
    exams = quiz['results']
    id_exams=[]
    for exam in exams:
          id_exam = exam['id']['raw']
          id_exams.append(id_exam)
    return id_exams

def get_answer(id_exam):
      conn = http.client.HTTPSConnection("studio-gw.eduquiz.io.vn")
      payload = ''
      headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': 'Bearer 568697|hb69N4oJ0hXbdo6UkWO3JHDVcDplwRRFnrOqVlbM',
        'chanel-quiz': 'phu-cong',
        'origin': 'https://eduquiz.vn',
        'priority': 'u=1, i',
        'referer': 'https://eduquiz.vn/',
        'sec-ch-ua': '"Opera";v="111", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 OPR/111.0.0.0',
        'x-requested-with': 'XMLHttpRequest'
      }  
      conn.request("GET", f"/quiz-chanel/public/api/v1/exams/{id_exam}/sections?bizapp=EDUQUIZ&is_question_shuffle=0&is_answer_shuffle=0&allow_access_exam=true", payload, headers)
      res = conn.getresponse()
      data = res.read()
      quiz_data = json.loads(data.decode("utf-8"))
      parsed_questions=[]
      questions = quiz_data['data'][0]['questions']
      for question in questions:
            parsed_question = {}
            parsed_question['question'] = {}
            parsed_question['question']['name'] = question["name"]
            for answer in question['answers']:
                  if answer['is_correct'] is True:
                    parsed_question['question']['answer'] = answer['option']
            parsed_questions.append(parsed_question)
      return  parsed_questions
      


FILTER_SCHOOLS = get_schools()
exams = get_exams(FILTER_SCHOOLS[0])
answers = get_answer(exams[0])




