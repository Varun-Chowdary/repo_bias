from BiasAsker import *
from apis import *
from multiprocessing.dummy import Process

import json
from transformers import AutoModelForCausalLM, AutoTokenizer, T5Tokenizer, T5ForConditionalGeneration, BlenderbotTokenizer, BlenderbotForConditionalGeneration
from transformers import TextGenerationPipeline, AutoModelWithLMHead
import torch
import os
import openai
import abc
import time
import urllib
import requests
from requests.structures import CaseInsensitiveDict
import ast
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.nlp.v20190408 import nlp_client, models
from cleverwrap import CleverWrap
import spacy

from experiment import ask

asker = BiasAsker("en")
status = asker.get_status()
print(status)

bot = GPT3()

ask(asker, bot, "gpt3")

stats = asker.get_status(bot)
print(stats)


