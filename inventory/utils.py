def upload_file_name(instance, filename):
    return f'/uploads/upload_file/{instance.id}_{filename}'