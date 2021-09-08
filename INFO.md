**Objectives**

## Explain the difference between internationalization and localization

- [x] Add language prefixes to URLs
- [x] Translate templates
- [x] Allow users to switch between languages
- [x] Translate models
- [x] Add locale-support

**Internationalization vs Localization**
   ------------------------------------
## Internationlization and Localization represent two sides to the same coin.

- Internationalization:
    Represents by i18n
    processing of developing the application so that it can be used by different locales.
    Generally handled by developers

- Localization:
    Represents by l10n
    Process for translating the application to a particular language and locale.
    Generally handled by translators.

The GNU gettext toolkit is used to generate and manage a plain text file represents a language known as the message file.
Message file ends with .po extension.
Another file is generated for each language once the translation is done - ends with .mo extension. Known as the compiled translation.

For Windows, the steps to install can be found [gettext](https://mlocati.github.io/articles/gettext-iconv-windows.html).

**Django Internationalization Framework:**

```
    LANGUAGE_CODE = 'en'
    TIME_ZONE= 'UTC'
    USE_I18N = True
    USE_L1ON = True
    USE_TZ = True

    LANGUAGES = (
        ('en', _('EN')),
        ('de', _('DE')),
    )

    MIDDLAWARE = [
        'django.middleware.locale.LocaleMiddleware',
    ]
```
## Command:
django-admin makemessages --all --ignore=venv
django-admin compilemessages --ignore=venv

## Add Language Prefix

```
    from djanago.corf.urls.i18n import i18n_patterns

    urlpatterns = i18n_patterns(
        path('admin/', admin.site.urls),
    )
```

## Allowing Users to Switch Languages

```
    {% load i18n %}
```

## Retrieved the current language using the {% get_current_language %} tag.

```
    {% get_current_language as CURRENT_LANGUAGE %}
```

## Retrieved the available language defined in the LANGUAGES setting using the {% get_available_languages %} tag.

```
    {% get_available_languages as AVAILABLE_LANGUAGES %}
```

## Then  using the {% get_language_info_list %} tag to enable the language attributes.

```
    {% get_language_info_list %}
```
