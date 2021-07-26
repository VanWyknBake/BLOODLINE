from django.contrib import admin
from .models import Home, About, Profile, Category, Results, Skills, Portfolio, Store, Streamers, Tourn


# Home
admin.site.register(Home)

# About
class ProfileInline(admin.TabularInline):
    model = Profile
    extra = 1

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
     inlines = [
        ProfileInline,
    ]
# Tournements
admin.site.register(Tourn)
# Skills
class SkillsInline(admin.TabularInline):
    model = Skills
    extra = 2

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
     inlines = [
        SkillsInline,
    ]


# Portfolio
admin.site.register(Portfolio)
admin.site.register(Streamers)
admin.site.register(Results)
admin.site.register(Store)
