class VeevaAPI:
    @staticmethod
    def get_object(object_type, object_id, token):
        # Logic to make GET request to Veeva API for object retrieval
        return f"Getting {object_type} with ID {object_id}"

    @staticmethod
    def create_object(object_data, token):
        # Logic to make POST request to Veeva API for object creation
        return f"Creating object with data: {object_data}"

    @staticmethod
    def update_object(object_id, updated_data, token):
        # Logic to make PUT request to Veeva API for object update
        return f"Updating object with ID {object_id} using data: {updated_data}"

    @staticmethod
    def delete_object(object_id, token):
        # Logic to make DELETE request to Veeva API for object deletion
        return f"Deleting object with ID {object_id}"
