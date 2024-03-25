# Coursurf API

The Course API provides endpoints to perform various operations related to courses.

## Endpoints

### Search Courses

- **Endpoint**: `/api/v1/courses/search`
- **Method**: GET
- **Description**: Retrieve a list of courses based on search criteria.
- **Parameters**:
  - `query` (String): The search query to filter courses.
  - `limit` (Integer): The maximum number of courses to return.
  - `offset` (Integer): The offset from where to start fetching courses.

### Semantic Search Courses

- **Endpoint**: `/api/v1/courses/semantic_search`
- **Method**: GET
- **Description**: Perform a semantic search for courses based on a given query.
- **Parameters**:
  - `query` (String): The search query for semantic search.
  - `limit` (Integer): The maximum number of courses to return.
  - `offset` (Integer): The offset from where to start fetching courses.

### Filter Course

- **Endpoint**: `/api/v1/courses/filter`
- **Method**: GET
- **Description**: Filter courses based on various criteria.
- **Parameters**:
  - `category` (String): The category of the courses to filter.
  - `level` (String): The level of difficulty for the courses (e.g., beginner, intermediate, advanced).
  - `limit` (Integer): The maximum number of courses to return.
  - `offset` (Integer): The offset from where to start fetching courses.

### View Course

- **Endpoint**: `/api/v1/courses/view`
- **Method**: GET
- **Description**: View details of a specific course.
- **Parameters**:
  - `course_id` (String): The unique identifier of the course to view.

## Example Usage

### Search Courses

```
GET /api/v1/courses/search?query=java&limit=10&offset=0
```

### Semantic Search Courses

```
GET /api/v1/courses/semantic_search?query=programming&limit=5&offset=0
```

### Filter Course

```
GET /api/v1/courses/filter?category=web development&level=beginner&limit=5&offset=0
```

### View Course

```
GET /api/v1/courses/view?course_id=123456
```
