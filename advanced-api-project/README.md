# API Views for Book Model

## Endpoints

- **GET /api/books/**  
  Returns a list of all books. Public access.

- **GET /api/books/<id>/**  
  Returns details of a single book by ID. Public access.

- **POST /api/books/create/**  
  Creates a new book. Requires authentication.

- **PUT /PATCH /api/books/<id>/update/**  
  Updates an existing book by ID. Requires authentication.

- **DELETE /api/books/<id>/delete/**  
  Deletes a book by ID. Requires authentication.

## Permissions

- Read operations are open to everyone.
- Write operations (create, update, delete) require the user to be authenticated.

## Customization Hooks

- `perform_create` and `perform_update` methods can be overridden to add custom save logic.
- Additional filters and permission classes can be added per view as needed.

