package com.example.Coursurf.Server.controller;

import com.example.Coursurf.Server.model.University;

import com.mongodb.DBObject;
import com.mongodb.client.MongoClients;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoDatabase;
import org.bson.Document;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.List;
import com.mongodb.DBObject;
import com.mongodb.MongoException;
import com.mongodb.client.MongoClients;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoDatabase;
import org.bson.Document;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
@RequestMapping("/api/v1")
public class CourseController {
    private final MongoTemplate mongoTemplate;

    @Autowired
    public CourseController(MongoTemplate mongoTemplate) {
        this.mongoTemplate = mongoTemplate;
    }


    @GetMapping("/")
    public String base_function() {
        return "Hello, World!";
    }

    @GetMapping("/courses")
    public String hello() {
        try {
            // MongoClients.create(mongoTemplate.getDb().getMongoClient().getConnectionString().getValue());
            String dbName = mongoTemplate.getDb().getName();
            return "Hello, World! Database connection successful.";
        } catch (MongoException e) {
            return "Hello, World! Database connection failed: " + e.getMessage();
        }
    }

    // @GetMapping("/get_courses")
    // public ResponseEntity<List<University>> getTopCourses() {
    //     try {
    //         List<University> allCourses = mongoTemplate.findAll(University.class);
    //         if (allCourses.isEmpty()) {
    //             return ResponseEntity.status(HttpStatus.NOT_FOUND).body(allCourses); // No courses found, return empty list
    //         }

    //         // if (allCourses.size() > 20) {
    //         //     Random random = new Random();
    //         //     int startIndex = random.nextInt(allCourses.size() - 20);
    //         //     return ResponseEntity.ok(allCourses.subList(startIndex, startIndex + 20));
    //         // } else {
    //         return ResponseEntity.ok(allCourses);
    //         // }
    //     } catch (Exception e) {
    //         return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(null); // Internal server error
    //     }
    // }



    @GetMapping("/get_courses")
    public ResponseEntity<List<Document>> getTopCourses() {
        try {
            // Connect to the MongoDB database
            try (com.mongodb.client.MongoClient mongoClient = MongoClients.create("mongodb+srv://adithyask:adithyask@courses.9v6zz7i.mongodb.net/<your-database-name>?retryWrites=true&w=majority&appName=Courses")) {
                MongoDatabase database = mongoClient.getDatabase("courses");
                MongoCollection<Document> collection = database.getCollection("universities");

                // Retrieve all documents from the collection
                List<Document> allCourses = new ArrayList<>();
                for (Document document : collection.find()) {
                    allCourses.add(document);
                }

                if (allCourses.isEmpty()) {
                    return ResponseEntity.status(HttpStatus.NOT_FOUND).body(allCourses); // No courses found, return empty list
                }

                return ResponseEntity.ok(allCourses);
            }
        } catch (Exception e) {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(null); // Internal server error
        }
    }

    @GetMapping("/courses/search")
    public String searchCourses() {
        return "Search Courses Endpoint";
    }

    @GetMapping("/courses/semantic_search")
    public String semanticSearchCourses() {
        return "Semantic Search Courses Endpoint";
    }

    @GetMapping("/courses/filter")
    public String filterCourse() {
        return "Filter Course Endpoint";
    }

    @GetMapping("/courses/view")
    public String viewCourse() {
        return "View Course Endpoint";
    }

}
