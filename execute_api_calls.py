import urllib.request, json, sys

sys.stdout.reconfigure(encoding='utf-8')

test_results = {}

print("=== 1. POST /students/save (Mohamed LACHGAR) ===")
req1 = urllib.request.Request(
    "http://localhost:8080/students/save",
    data=json.dumps({"nom": "LACHGAR", "prenom": "Mohamed", "dateNaissance": "1985-09-01"}).encode('utf-8'),
    headers={"Content-Type": "application/json"}
)
with urllib.request.urlopen(req1) as r1:
    res1 = json.loads(r1.read().decode())
    print("HTTP Status:", r1.status)
    print("Response Body:", json.dumps(res1, indent=2))
    test_results['post_student1'] = res1

print("\n=== 2. POST /students/save (Fatima BENANI) ===")
req2 = urllib.request.Request(
    "http://localhost:8080/students/save",
    data=json.dumps({"nom": "BENANI", "prenom": "Fatima", "dateNaissance": "1985-11-15"}).encode('utf-8'),
    headers={"Content-Type": "application/json"}
)
with urllib.request.urlopen(req2) as r2:
    res2 = json.loads(r2.read().decode())
    print("HTTP Status:", r2.status)
    print("Response Body:", json.dumps(res2, indent=2))
    test_results['post_student2'] = res2

print("\n=== 3. POST /students/save (Yassine ALAMI) ===")
req3 = urllib.request.Request(
    "http://localhost:8080/students/save",
    data=json.dumps({"nom": "ALAMI", "prenom": "Yassine", "dateNaissance": "1990-04-20"}).encode('utf-8'),
    headers={"Content-Type": "application/json"}
)
with urllib.request.urlopen(req3) as r3:
    res3 = json.loads(r3.read().decode())
    print("HTTP Status:", r3.status)
    print("Response Body:", json.dumps(res3, indent=2))
    test_results['post_student3'] = res3

print("\n=== 4. GET /students/all ===")
with urllib.request.urlopen("http://localhost:8080/students/all") as r4:
    res4 = json.loads(r4.read().decode())
    print("HTTP Status:", r4.status)
    print("Response Body:", json.dumps(res4, indent=2))
    test_results['get_all'] = res4

print("\n=== 5. GET /students/count ===")
with urllib.request.urlopen("http://localhost:8080/students/count") as r5:
    res5 = json.loads(r5.read().decode())
    print("HTTP Status:", r5.status)
    print("Total Students Count:", res5)
    test_results['get_count'] = res5

print("\n=== 6. GET /students/byYear ===")
with urllib.request.urlopen("http://localhost:8080/students/byYear") as r6:
    res6 = json.loads(r6.read().decode())
    print("HTTP Status:", r6.status)
    print("Response Body (Statistics):", json.dumps(res6, indent=2))
    test_results['get_by_year'] = res6

print("\n=== 7. GET /v3/api-docs (OpenAPI 3.0 Documentation) ===")
with urllib.request.urlopen("http://localhost:8080/v3/api-docs") as r7:
    res7 = json.loads(r7.read().decode())
    print("HTTP Status:", r7.status)
    print("OpenAPI Title:", res7.get('info', {}).get('title'))
    print("OpenAPI Version:", res7.get('info', {}).get('version'))
    print("Paths documented:", list(res7.get('paths', {}).keys()))
    test_results['openapi'] = res7

print("\n=== 8. GET /swagger-ui/index.html (Swagger UI Web Interface) ===")
with urllib.request.urlopen("http://localhost:8080/swagger-ui/index.html") as r8:
    html_content = r8.read().decode()
    print("HTTP Status:", r8.status)
    print("Swagger HTML Size:", len(html_content), "bytes")
    test_results['swagger_ui_status'] = r8.status

print("\n=== 9. DELETE /students/delete/1 ===")
req_del = urllib.request.Request("http://localhost:8080/students/delete/1", method="DELETE")
with urllib.request.urlopen(req_del) as r9:
    print("HTTP Status:", r9.status, "(204 No Content expected)")
    test_results['delete_status'] = r9.status

print("\n=== 10. GET /students/count (after deletion) ===")
with urllib.request.urlopen("http://localhost:8080/students/count") as r10:
    res10 = json.loads(r10.read().decode())
    print("HTTP Status:", r10.status)
    print("Total Students Count after deletion:", res10)
    test_results['get_count_after_del'] = res10

with open(r"C:\Users\admin\.gemini\antigravity-ide\scratch\TP-6-Spring-Boot-et-Swagger-Documentation-d-API-Microservices\test_execution_results.json", "w", encoding='utf-8') as out:
    json.dump(test_results, out, indent=2)

print("\nAll endpoints tested successfully!")
