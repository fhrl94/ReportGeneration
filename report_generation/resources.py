from import_export import resources
from .models import EmployeesInfo


class EmployeesInfoResource(resources.ModelResource):
    class Meta:
        model = EmployeesInfo  # fields = ('name', 'code', 'level', 'emp_status')  # exclude = ('id')


