

enum Major {
    ... // majors
}

struct Course {
    name: String,
    id: u32,
    required: Vec<Course>,
    topics: Vec<Major>,
}