from django.contrib import admin
from django.template.response import TemplateResponse

class CustomAdminSite(admin.AdminSite):
    def index(self, request, extra_context=None):
        return TemplateResponse(request, "admin/dashboard.html", extra_context or {})

custom_admin_site = CustomAdminSite(name="custom_admin")


from products.models import Category, Product
from django.db import models
from orders.models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Category, site=custom_admin_site)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)


from django.utils.html import format_html

@admin.register(Product, site=custom_admin_site)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "stock", "image_tag", "created_at", "updated_at")
    list_filter = ("category",)
    search_fields = ("name",)

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height:40px;max-width:40px;" />', obj.image.url)
        return ""
    image_tag.short_description = "Image"

    formfield_overrides = {
        # Use Bootstrap classes for form fields
        models.CharField: {"widget": admin.widgets.AdminTextInputWidget(attrs={"class": "form-control"})},
        models.TextField: {"widget": admin.widgets.AdminTextareaWidget(attrs={"class": "form-control"})},
        models.DecimalField: {"widget": admin.widgets.AdminTextInputWidget(attrs={"class": "form-control"})},
        models.PositiveIntegerField: {"widget": admin.widgets.AdminTextInputWidget(attrs={"class": "form-control"})},
        models.ImageField: {"widget": admin.widgets.AdminFileWidget(attrs={"class": "form-control"})},
    }

@admin.register(Order, site=custom_admin_site)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "customer_name", "customer_email", "status", "created_at")
    list_filter = ("status",)
    search_fields = ("customer_name", "customer_email")
    inlines = [OrderItemInline]
    actions = ["mark_as_processing", "mark_as_shipped", "mark_as_delivered", "mark_as_cancelled"]

    def mark_as_processing(self, request, queryset):
        queryset.update(status="processing")
    mark_as_processing.short_description = "Mark selected orders as Processing"

    def mark_as_shipped(self, request, queryset):
        queryset.update(status="shipped")
    mark_as_shipped.short_description = "Mark selected orders as Shipped"

    def mark_as_delivered(self, request, queryset):
        queryset.update(status="delivered")
    mark_as_delivered.short_description = "Mark selected orders as Delivered"

    def mark_as_cancelled(self, request, queryset):
        queryset.update(status="cancelled")
    mark_as_cancelled.short_description = "Mark selected orders as Cancelled"
