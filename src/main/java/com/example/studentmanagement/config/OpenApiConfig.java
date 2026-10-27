package com.example.studentmanagement.config;

import io.swagger.v3.oas.models.OpenAPI;
import io.swagger.v3.oas.models.info.Contact;
import io.swagger.v3.oas.models.info.Info;
import io.swagger.v3.oas.models.info.License;
import io.swagger.v3.oas.models.servers.Server;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.util.List;

/**
 * Configuration personnalisée de la documentation Swagger / OpenAPI (springdoc-openapi).
 */
@Configuration
public class OpenApiConfig {

    @Bean
    public OpenAPI customOpenAPI() {
        return new OpenAPI()
                .info(new Info()
                        .title("TP 6 : Spring Boot et Swagger - Documentation d'API Microservices")
                        .version("1.0.0")
                        .description("Microservice Spring Boot complet de gestion des étudiants avec documentation interactive Swagger / OpenAPI. " +
                                "Permet d'effectuer les opérations CRUD et d'analyser les statistiques démographiques.")
                        .contact(new Contact()
                                .name("Youness Bakka")
                                .email("younessbakka7@gmail.com")
                                .url("https://github.com/younessbakka7"))
                        .license(new License()
                                .name("Apache 2.0")
                                .url("https://www.apache.org/licenses/LICENSE-2.0.html")))
                .servers(List.of(
                        new Server()
                                .url("http://localhost:8080")
                                .description("Serveur Local de Développement")));
    }
}
