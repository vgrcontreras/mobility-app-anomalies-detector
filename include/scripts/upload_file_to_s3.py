import os

import boto3
from botocore.exceptions import ClientError
from loguru import logger

from include.settings import settings


def upload_files_to_s3(
        file_name: str, bucket: str, object_name: str = None
) -> bool:
    """
    Upload file to an S3 bucket

    :param file_name: File to upload (path + file_name)
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: (bool) True if file was uploaded, else False
    """
    if object_name is None:
        object_name = os.path.basename(file_name)

    try:
        s3_client = boto3.client(
            's3',
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name=settings.AWS_REGION
        )
    except Exception as e:
        logger.error(f"Erro ao criar o cliente S3: {e}")
        return False

    try:
        s3_client.upload_file(file_name, bucket, object_name)
        logger.success(
            f"Upload bem-sucedido: {file_name} → s3://{bucket}/{object_name}"
        )
        return True
    except ClientError as e:
        logger.error(
            f"Erro ao fazer upload do arquivo {file_name} "
            f"para o bucket {bucket}: {e}"
        )
        return False
    except Exception as e:
        logger.exception(
            f"Erro inesperado ao fazer upload do arquivo {file_name}: {e}"
        )
        return False


def main_s3(folder_path: str) -> None:
    if not os.path.exists(folder_path):
        logger.warning(f"Pasta não encontrada: {folder_path}")
        return

    if not os.listdir(folder_path):
        logger.info(f"Pasta vazia: {folder_path}")
        return

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        if os.path.isfile(file_path):
            try:
                uploaded = upload_files_to_s3(file_path, settings.BUCKET_NAME)

                if uploaded:
                    os.remove(file_path)
                    logger.info(f"Arquivo removido após upload: {file_path}")
                else:
                    logger.warning(
                        f"Upload falhou, arquivo preservado: {file_path}"
                    )
            except Exception as e:
                logger.exception(
                    f"Erro ao processar o arquivo {file_path}: {e}"
                )
