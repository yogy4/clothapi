from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
import os
from flask import Flask, Blueprint, request, jsonify, render_template, abort, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt, JWTManager)

