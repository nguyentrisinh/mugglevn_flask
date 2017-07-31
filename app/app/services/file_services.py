import os
from werkzeug.utils import secure_filename
from .. import Config

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


class FileServices:

    def __init__(self):
        pass

    @staticmethod
    def allowed_file(filename):
        return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    @classmethod
    def upload_file(cls, path, request):
        # check if the post request has the file part
        if 'file' not in request.files:
            print 'No file part'
            # return redirect(request.url)
            return {"content": "No file part"}

        file_upload = request.files['file']

        # if user does not select file, browser also
        # submit a empty part without filename
        if file_upload.filename == '':
            print 'No selected file'
            return {"content": "No selected file"}

        if file_upload and cls.allowed_file(file_upload.filename):
            filename = secure_filename(file_upload.filename)

            # Create a full path of the storage that upload image in it
            full_path = '{}{}'.format(Config.UPLOAD_FOLDER, path)

            cls.check_folder(full_path)

            # Save the file in to correct path
            file_upload.save(os.path.join(full_path, filename))

            return {"content": os.path.join(full_path, filename)}

        return {"content": "final return"}

    # This method use to check full_path have already had dictionary or not
    # If not, this method will create a folder in it (just create a FINAL folder)
    # If parent folder doesn't have it will catch error
    @staticmethod
    def check_folder(full_path):

        if os.path.isdir(full_path) is False:
            os.mkdir(full_path)
