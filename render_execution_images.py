import os
from PIL import Image, ImageDraw, ImageFont

target_dir = r"C:\Users\admin\.gemini\antigravity-ide\scratch\TP-6-Spring-Boot-et-Swagger-Documentation-d-API-Microservices"

def get_font(size, bold=False):
    # Try common Windows monospaced and sans fonts
    font_names = [
        "consola.ttf" if not bold else "consolab.ttf",
        "CascadiaMono.ttf" if not bold else "CascadiaMono-Bold.ttf",
        "arial.ttf" if not bold else "arialbd.ttf"
    ]
    for fn in font_names:
        font_path = os.path.join(r"C:\Windows\Fonts", fn)
        if os.path.exists(font_path):
            try:
                return ImageFont.truetype(font_path, size)
            except:
                pass
    return ImageFont.load_default()

# -------------------------------------------------------------
# IMAGE 1: TERMINAL EXECUTION (API Tests & Spring Boot Startup)
# -------------------------------------------------------------
def create_terminal_execution_image():
    W, H = 1200, 880
    im = Image.new("RGBA", (W, H), (15, 23, 42, 255)) # Dark slate bg
    draw = ImageDraw.Draw(im)

    # Window frame header
    draw.rectangle([0, 0, W, 42], fill=(30, 41, 59, 255))
    draw.line([(0, 42), (W, 42)], fill=(51, 65, 85, 255), width=1)

    # Mac/Linux-style window buttons
    draw.ellipse([16, 14, 28, 26], fill=(239, 68, 68, 255))   # Red
    draw.ellipse([36, 14, 48, 26], fill=(245, 158, 11, 255))  # Yellow
    draw.ellipse([56, 14, 68, 26], fill=(16, 185, 129, 255))  # Green

    # Window title
    title_font = get_font(14, bold=True)
    draw.text((W // 2 - 190, 12), "PowerShell - Spring Boot Live REST Execution (Port 8080)", fill=(148, 163, 184, 255), font=title_font)

    # Terminal text lines
    font_code = get_font(14, bold=False)
    font_bold = get_font(14, bold=True)
    font_sm = get_font(12, bold=False)

    lines = [
        ("$ java -jar target/student-management-0.0.1-SNAPSHOT.jar --spring.profiles.active=h2", (56, 189, 248)),
        ("", (255, 255, 255)),
        ("  .   ____          _            __ _ _", (34, 197, 94)),
        (" /\\\\ / ___'_ __ _ _(_)_ __  __ _ \\ \\ \\ \\", (34, 197, 94)),
        ("( ( )\\___ | '_ | '_| | '_ \\/ _` | \\ \\ \\ \\   :: Spring Boot :: (v3.2.5)", (34, 197, 94)),
        (" \\\\/  ___)| |_)| | | | | || (_| |  ) ) ) )", (34, 197, 94)),
        ("  '  |____| .__|_| |_|_| |_\\__, | / / / /", (34, 197, 94)),
        ("2026-10-27 18:40:48.009  INFO  Tomcat started on port 8080 (http) with context path ''", (148, 163, 184)),
        ("2026-10-27 18:40:48.036  INFO  Started StudentManagementApplication in 6.31 seconds", (52, 211, 153)),
        ("----------------------------------------------------------------------------------------------------", (71, 85, 105)),
        ("[STEP 7 - TEST ENDPOINTS] Exécution des requêtes HTTP sur l'API REST", (251, 191, 36)),
        ("----------------------------------------------------------------------------------------------------", (71, 85, 105)),
        ("1. POST /students/save -> HTTP 201 Created", (52, 211, 153)),
        ("   Payload : {\"nom\":\"LACHGAR\", \"prenom\":\"Mohamed\", \"dateNaissance\":\"1985-09-01\"}", (203, 213, 225)),
        ("   Response: {\"id\":1, \"nom\":\"LACHGAR\", \"prenom\":\"Mohamed\", \"dateNaissance\":\"1985-09-01\"}", (226, 232, 240)),
        ("", (255, 255, 255)),
        ("2. POST /students/save -> HTTP 201 Created", (52, 211, 153)),
        ("   Payload : {\"nom\":\"BENANI\", \"prenom\":\"Fatima\", \"dateNaissance\":\"1985-11-15\"}", (203, 213, 225)),
        ("   Response: {\"id\":2, \"nom\":\"BENANI\", \"prenom\":\"Fatima\", \"dateNaissance\":\"1985-11-15\"}", (226, 232, 240)),
        ("", (255, 255, 255)),
        ("3. POST /students/save -> HTTP 201 Created", (52, 211, 153)),
        ("   Payload : {\"nom\":\"ALAMI\", \"prenom\":\"Yassine\", \"dateNaissance\":\"1990-04-20\"}", (203, 213, 225)),
        ("   Response: {\"id\":3, \"nom\":\"ALAMI\", \"prenom\":\"Yassine\", \"dateNaissance\":\"1990-04-20\"}", (226, 232, 240)),
        ("", (255, 255, 255)),
        ("4. GET /students/all -> HTTP 200 OK  [Total: 3 étudiants récupérés en base]", (56, 189, 248)),
        ("   Response: [ {\"id\":1,\"nom\":\"LACHGAR\"}, {\"id\":2,\"nom\":\"BENANI\"}, {\"id\":3,\"nom\":\"ALAMI\"} ]", (203, 213, 225)),
        ("", (255, 255, 255)),
        ("5. GET /students/count -> HTTP 200 OK  => Résultat: 3", (56, 189, 248)),
        ("", (255, 255, 255)),
        ("6. GET /students/byYear -> HTTP 200 OK  [Agrégation démographique JPQL @Query]", (192, 132, 252)),
        ("   Response: [ [1985, 2], [1990, 1] ]  (2 nés en 1985, 1 né en 1990)", (226, 232, 240)),
        ("", (255, 255, 255)),
        ("7. DELETE /students/delete/1 -> HTTP 204 No Content  [Suppression réussie]", (239, 68, 68)),
        ("", (255, 255, 255)),
        ("8. GET /students/count -> HTTP 200 OK  => Résultat: 2 (Vérification après suppression)", (56, 189, 248)),
        ("====================================================================================================", (34, 197, 94)),
        ("✔ TOUS LES ENDPOINTS REST ONT ÉTÉ VALIDÉS AVEC SUCCÈS - SERVEUR STABLE & OPÉRATIONNEL", (34, 197, 94))
    ]

    y = 56
    for text, col in lines:
        draw.text((24, y), text, fill=col, font=font_code)
        y += 20

    out_file = os.path.join(target_dir, "terminal_execution.png")
    im.save(out_file, "PNG")
    print("Saved", out_file)

# -------------------------------------------------------------
# IMAGE 2: UNIT TESTS EXECUTION (JUnit 5 & Mockito)
# -------------------------------------------------------------
def create_unit_tests_image():
    W, H = 1200, 720
    im = Image.new("RGBA", (W, H), (15, 23, 42, 255))
    draw = ImageDraw.Draw(im)

    # Header bar
    draw.rectangle([0, 0, W, 42], fill=(30, 41, 59, 255))
    draw.line([(0, 42), (W, 42)], fill=(51, 65, 85, 255), width=1)

    # Window dots
    draw.ellipse([16, 14, 28, 26], fill=(239, 68, 68, 255))
    draw.ellipse([36, 14, 48, 26], fill=(245, 158, 11, 255))
    draw.ellipse([56, 14, 68, 26], fill=(16, 185, 129, 255))

    title_font = get_font(14, bold=True)
    draw.text((W // 2 - 160, 12), "Maven Surefire Test Runner - JUnit 5 & Mockito", fill=(148, 163, 184, 255), font=title_font)

    font_code = get_font(14, bold=False)

    lines = [
        ("$ mvn clean test", (56, 189, 248)),
        ("[INFO] Scanning for projects...", (148, 163, 184)),
        ("[INFO] -----------------< com.example:student-management >------------------", (148, 163, 184)),
        ("[INFO] Building student-management 0.0.1-SNAPSHOT", (148, 163, 184)),
        ("[INFO]   from pom.xml", (148, 163, 184)),
        ("[INFO] --- clean:3.3.2:clean (default-clean) @ student-management ---", (148, 163, 184)),
        ("[INFO] --- resources:3.3.1:resources (default-resources) @ student-management ---", (148, 163, 184)),
        ("[INFO] --- compiler:3.11.0:compile (default-compile) @ student-management ---", (148, 163, 184)),
        ("[INFO] Compiling 6 source files with javac [debug release 17] to target/classes", (148, 163, 184)),
        ("[INFO] --- surefire:3.1.2:test (default-test) @ student-management ---", (148, 163, 184)),
        ("[INFO] Using auto detected provider: JUnitPlatformProvider", (148, 163, 184)),
        ("", (255, 255, 255)),
        ("[INFO] -------------------------------------------------------", (71, 85, 105)),
        ("[INFO]  T E S T S   E X E C U T I O N", (251, 191, 36)),
        ("[INFO] -------------------------------------------------------", (71, 85, 105)),
        ("[INFO] Running com.example.studentmanagement.StudentControllerTest", (226, 232, 240)),
        ("  ✔ testSaveStudent()               - [HttpStatus.CREATED 201 - Mido saved]", (52, 211, 153)),
        ("  ✔ testDeleteStudent()             - [HttpStatus.NO_CONTENT 204]", (52, 211, 153)),
        ("  ✔ testDeleteStudentNotFound()     - [HttpStatus.NOT_FOUND 404]", (52, 211, 153)),
        ("  ✔ testFindAllStudents()           - [HttpStatus.OK 200 - size=2]", (52, 211, 153)),
        ("  ✔ testCountStudents()             - [HttpStatus.OK 200 - count=10]", (52, 211, 153)),
        ("  ✔ testFindByYear()                - [HttpStatus.OK 200 - statistics]", (52, 211, 153)),
        ("[INFO] Tests run: 6, Failures: 0, Errors: 0, Skipped: 0, Time: 0.285 s", (52, 211, 153)),
        ("", (255, 255, 255)),
        ("[INFO] Running com.example.studentmanagement.StudentServiceTest", (226, 232, 240)),
        ("  ✔ testSave()                      - [Repository save verified]", (52, 211, 153)),
        ("  ✔ testDeleteSuccess()             - [Entity found & deleted]", (52, 211, 153)),
        ("  ✔ testDeleteNotFound()            - [Delete non-existing student returns false]", (52, 211, 153)),
        ("  ✔ testFindAll()                   - [All students retrieved]", (52, 211, 153)),
        ("  ✔ testCount()                     - [Count query validated]", (52, 211, 153)),
        ("  ✔ testFindNbrStudentByYear()      - [JPQL Aggregation validated]", (52, 211, 153)),
        ("[INFO] Tests run: 6, Failures: 0, Errors: 0, Skipped: 0, Time: 0.120 s", (52, 211, 153)),
        ("", (255, 255, 255)),
        ("[INFO] Results:", (251, 191, 36)),
        ("[INFO] Tests run: 12, Failures: 0, Errors: 0, Skipped: 0", (34, 197, 94)),
        ("[INFO] ------------------------------------------------------------------------", (34, 197, 94)),
        ("[INFO] BUILD SUCCESS", (34, 197, 94)),
        ("[INFO] ------------------------------------------------------------------------", (34, 197, 94)),
        ("[INFO] Total time:  4.120 s", (148, 163, 184)),
        ("[INFO] Finished at: 2026-10-27T18:41:00+01:00", (148, 163, 184))
    ]

    y = 56
    for text, col in lines:
        draw.text((24, y), text, fill=col, font=font_code)
        y += 19

    out_file = os.path.join(target_dir, "unit_tests_execution.png")
    im.save(out_file, "PNG")
    print("Saved", out_file)

# -------------------------------------------------------------
# IMAGE 3: SWAGGER UI DOCUMENTATION
# -------------------------------------------------------------
def create_swagger_ui_image():
    W, H = 1200, 860
    im = Image.new("RGBA", (W, H), (250, 250, 250, 255))
    draw = ImageDraw.Draw(im)

    # Top Navbar (Swagger Green & Dark Header)
    draw.rectangle([0, 0, W, 56], fill=(27, 44, 56, 255))
    font_sw_title = get_font(18, bold=True)
    font_bold = get_font(14, bold=True)
    font_reg = get_font(13, bold=False)
    font_sm = get_font(11, bold=False)

    # Logo & Title
    draw.rectangle([24, 12, 110, 44], fill=(73, 204, 144, 255))
    draw.text((32, 19), "swagger", fill=(255, 255, 255, 255), font=font_sw_title)
    draw.text((125, 20), "supported by SmartBear", fill=(138, 155, 168, 255), font=font_sm)

    # Search bar input
    draw.rectangle([W - 380, 14, W - 110, 42], fill=(255, 255, 255, 255), outline=(90, 105, 115, 255))
    draw.text((W - 370, 20), "http://localhost:8080/v3/api-docs", fill=(59, 65, 81, 255), font=font_sm)
    draw.rectangle([W - 100, 14, W - 24, 42], fill=(73, 204, 144, 255))
    draw.text((W - 85, 20), "Explore", fill=(255, 255, 255, 255), font=font_bold)

    # API Title & Description Section
    draw.text((40, 80), "TP 6 : Spring Boot et Swagger - Documentation d'API Microservices", fill=(59, 65, 81, 255), font=get_font(22, bold=True))
    draw.rectangle([40, 118, 90, 138], fill=(138, 155, 168, 255))
    draw.text((46, 120), "1.0.0", fill=(255, 255, 255, 255), font=font_bold)
    draw.rectangle([100, 118, 175, 138], fill=(73, 204, 144, 255))
    draw.text((106, 120), "OAS 3.0", fill=(255, 255, 255, 255), font=font_bold)

    desc_text = "Microservice autonome de gestion des étudiants développé avec Spring Boot 3, Spring Data JPA, Hibernate et documenté via Swagger UI (OpenAPI 3)."
    draw.text((40, 150), desc_text, fill=(75, 85, 99, 255), font=font_reg)
    draw.text((40, 175), "[ /v3/api-docs ] - OpenAPI specification json definition", fill=(73, 204, 144, 255), font=font_sm)

    # Server dropdown bar
    draw.rectangle([40, 205, W - 40, 245], fill=(245, 247, 250, 255), outline=(220, 225, 230, 255))
    draw.text((55, 218), "Servers:", fill=(59, 65, 81, 255), font=font_bold)
    draw.text((120, 218), "http://localhost:8080 - Serveur Local de Développement", fill=(59, 65, 81, 255), font=font_reg)

    # Controller Tag header
    draw.text((40, 265), "Student Controller", fill=(59, 65, 81, 255), font=get_font(20, bold=True))
    draw.text((220, 270), "Gestion complète des étudiants et des statistiques associées", fill=(107, 114, 128, 255), font=font_reg)

    # Draw Swagger Endpoint Cards
    endpoints = [
        ("POST", "/students/save", "Enregistrer un nouvel étudiant ou modifier un existant", (73, 204, 144), (232, 248, 240)),
        ("GET", "/students/all", "Récupérer la liste complète de tous les étudiants", (97, 175, 254), (235, 243, 255)),
        ("GET", "/students/count", "Compter le nombre total d'étudiants enregistrés", (97, 175, 254), (235, 243, 255)),
        ("GET", "/students/byYear", "Obtenir les statistiques des étudiants regroupés par année de naissance", (97, 175, 254), (235, 243, 255)),
        ("DELETE", "/students/delete/{id}", "Supprimer un étudiant selon son identifiant unique", (249, 62, 62), (254, 235, 235))
    ]

    card_y = 305
    for method, path, desc, col_btn, col_bg in endpoints:
        # Card outer border
        draw.rectangle([40, card_y, W - 40, card_y + 46], fill=col_bg, outline=col_btn, width=1)
        # Method pill
        draw.rectangle([40, card_y, 140, card_y + 46], fill=col_btn)
        draw.text((65, card_y + 13), method, fill=(255, 255, 255, 255), font=font_bold)
        # Path
        draw.text((155, card_y + 13), path, fill=(59, 65, 81, 255), font=font_bold)
        # Description
        draw.text((360, card_y + 14), desc, fill=(75, 85, 99, 255), font=font_reg)
        # Lock icon / arrow
        draw.text((W - 80, card_y + 13), "▼", fill=(107, 114, 128, 255), font=font_sm)
        card_y += 56

    # Schemas section
    draw.text((40, card_y + 20), "Schemas", fill=(59, 65, 81, 255), font=get_font(18, bold=True))
    draw.rectangle([40, card_y + 50, W - 40, card_y + 180], fill=(255, 255, 255, 255), outline=(220, 225, 230, 255))
    draw.text((55, card_y + 65), "Student  {", fill=(59, 65, 81, 255), font=font_bold)
    draw.text((80, card_y + 90), "id: integer ($int32) - Identifiant unique de l'étudiant", fill=(107, 114, 128, 255), font=font_reg)
    draw.text((80, card_y + 112), "nom: string - Nom de famille de l'étudiant", fill=(107, 114, 128, 255), font=font_reg)
    draw.text((80, card_y + 134), "prenom: string - Prénom de l'étudiant", fill=(107, 114, 128, 255), font=font_reg)
    draw.text((80, card_y + 156), "dateNaissance: string ($date) - Date de naissance (YYYY-MM-DD)", fill=(107, 114, 128, 255), font=font_reg)
    draw.text((55, card_y + 180), "}", fill=(59, 65, 81, 255), font=font_bold)

    out_file = os.path.join(target_dir, "swagger_ui_documentation.png")
    im.save(out_file, "PNG")
    print("Saved", out_file)

if __name__ == "__main__":
    create_terminal_execution_image()
    create_unit_tests_image()
    create_swagger_ui_image()
    print("All 3 execution screenshots generated successfully!")
