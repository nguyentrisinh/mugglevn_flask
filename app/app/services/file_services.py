import os
from flask import redirect, url_for
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
    def upload_file(cls, request):
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
            print os.path.join(Config.UPLOAD_FOLDER, filename)
            file_upload.save(os.path.join(Config.UPLOAD_FOLDER, filename))

            # return redirect(url_for('uploaded_file',
            #                         filename=filename))
            # return {"content": "{}".format(redirect(url_for('upload_file', filename=filename)))}

            return {"content": "Hello world"}

        return {"content": "final return"}
