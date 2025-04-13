from .ds_salary.routes import ds_salary_bp
from .sleep_disorder.routes import sleep_disorder_bp
from .ecomm_delivery.routes import ecomm_delivery_bp

#! To add other projects
# from .project2.routes import project2_bp
# from .project3.routes import project3_bp

project_blueprints = [ds_salary_bp, sleep_disorder_bp, ecomm_delivery_bp]
#! While adding new projects, add them here as well. (Example: [ds_salary_bp, project2_bp, project3_bp])
