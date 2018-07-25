# coding: utf-8

import os
import os.path as osp

from supervisely_lib import mkdir


HOST_DIR = None
SERVER_ADDRESS = None
TOKEN = None
TASKS_DOCKER_LABEL = None

DOCKER_LOGIN = None
DOCKER_PASSWORD = None
DOCKER_REGISTRY = None

AGENT_TASKS_DIR_HOST = None

DELETE_TASK_DIR_ON_FINISH = True

AGENT_ROOT_DIR = '/sly_agent'
AGENT_LOG_DIR = osp.join(AGENT_ROOT_DIR, 'logs')
AGENT_TASKS_DIR = osp.join(AGENT_ROOT_DIR, 'tasks')
AGENT_TMP_DIR = osp.join(AGENT_ROOT_DIR, 'tmp')
AGENT_IMPORT_DIR = osp.join(AGENT_ROOT_DIR, 'import')
AGENT_STORAGE_DIR = osp.join(AGENT_ROOT_DIR, 'storage')

WITH_LOCAL_STORAGE = None
UPLOAD_RESULT_IMAGES = None
PULL_ALWAYS = None

mkdir(AGENT_LOG_DIR)
mkdir(AGENT_TASKS_DIR)
mkdir(AGENT_STORAGE_DIR)
mkdir(AGENT_TMP_DIR)
mkdir(AGENT_IMPORT_DIR)
os.chmod(AGENT_IMPORT_DIR, 0o777)  # octal


NETW_CHUNK_SIZE = 1048576

BATCH_SIZE_GET_IMAGES_INFO = 100
BATCH_SIZE_DOWNLOAD_IMAGES = 20
BATCH_SIZE_DOWNLOAD_ANNOTATIONS = 100
BATCH_SIZE_UPLOAD_IMAGES = 20
BATCH_SIZE_UPLOAD_ANNOTATIONS = 100
BATCH_SIZE_LOG = 100