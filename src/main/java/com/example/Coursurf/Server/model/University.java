package com.example.Coursurf.Server.model;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@Document(collection = "universities")
public class University {

    @Id
    private String id;

    private String name;
    private String description;
    private String university;
    private String universityTag;
    private String link;
    private String provider;
    private String duration;
    private String pricing;

    // Constructors, getters, and setters
    public University() {
    }

    public University(String id, String name, String description, String university, String universityTag, String link, String provider, String duration, String pricing) {
        this.id = id;
        this.name = name;
        this.description = description;
        this.university = university;
        this.universityTag = universityTag;
        this.link = link;
        this.provider = provider;
        this.duration = duration;
        this.pricing = pricing;
    }
}