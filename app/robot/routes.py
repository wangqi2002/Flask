from flask import Blueprint, render_template, request, redirect, url_for

robot_bp = Blueprint('auth', __name__)

@robot_bp.route('/')
def index():
    return "robot"
