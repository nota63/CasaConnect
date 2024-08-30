from django.contrib import admin
from .models import Workers, Role, Purchase, Cancel, Complaint, Feedback, Payments, Jobs,JobApplications,Contact,Discounts


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('user', 'work',)
    list_filter = ('user', 'work',)
    search_fields = ('work',)


class CancelAdmin(admin.ModelAdmin):
    list_filter = ('user', 'work',)
    list_display = ('user', 'work',)


class ComplaintAdmin(admin.ModelAdmin):
    list_filter = ('user', 'work',)
    list_display = ('user', 'work',)
    search_fields = ('user', 'work',)


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user', 'work',)
    list_filter = ('user', 'work',)
    search_fields = ('user', 'work',)


class JobAdmin(admin.ModelAdmin):
    list_filter = ('title', 'package',)
    list_display = ('title', 'package',)
    search_fields = ('title',)


# Register your models here.
admin.site.register(Workers)
admin.site.register(Role)
admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(Cancel, CancelAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Payments)
admin.site.register(Jobs, JobAdmin)
admin.site.register(JobApplications)
admin.site.register(Contact)
admin.site.register(Discounts)

