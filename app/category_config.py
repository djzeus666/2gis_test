# Configuration for 10 unique visual template designs for demo sites

TEMPLATES_CONFIG = {
    1: {
        "id": 1,
        "name": "Dark Neon Cyber",
        "description": "Темный неоновый стиль с динамическим градиентом и подсвеченными акцентами",
        "style_class": "template-cyber",
        "bg_class": "bg-slate-950 text-slate-100",
        "header_class": "bg-slate-900/80 backdrop-blur-md border-b border-slate-800",
        "hero_class": "bg-gradient-to-br from-slate-950 via-zinc-900 to-indigo-950",
        "card_class": "bg-slate-900/90 border border-slate-800 hover:border-indigo-500/50 shadow-xl rounded-2xl",
        "primary_btn_class": "bg-gradient-to-r from-indigo-500 to-purple-600 hover:from-indigo-600 hover:to-purple-700 text-white font-bold shadow-lg shadow-indigo-500/25",
        "accent_text_class": "text-indigo-400",
        "badge_class": "bg-indigo-500/10 text-indigo-400 border border-indigo-500/30",
        "font_family": "font-sans",
        "hero_layout": "split-right",
        "border_radius": "rounded-2xl"
    },
    2: {
        "id": 2,
        "name": "Clean Modern Light",
        "description": "Светлый минималистичный дизайн с высокой читаемостью и контрастом",
        "style_class": "template-light",
        "bg_class": "bg-gray-50 text-gray-900",
        "header_class": "bg-white/90 backdrop-blur-md border-b border-gray-200 shadow-sm",
        "hero_class": "bg-gradient-to-br from-blue-50 via-white to-sky-50 text-gray-900",
        "card_class": "bg-white border border-gray-100 shadow-md hover:shadow-xl rounded-2xl transition-all",
        "primary_btn_class": "bg-blue-600 hover:bg-blue-700 text-white font-bold shadow-md shadow-blue-500/20",
        "accent_text_class": "text-blue-600",
        "badge_class": "bg-blue-100 text-blue-800 border border-blue-200",
        "font_family": "font-sans",
        "hero_layout": "split-right",
        "border_radius": "rounded-2xl"
    },
    3: {
        "id": 3,
        "name": "Luxury Gold & Black",
        "description": "Премиальный стиль в темных и золотых тонах для бутиков и элитных услуг",
        "style_class": "template-luxury",
        "bg_class": "bg-stone-950 text-stone-100",
        "header_class": "bg-stone-900/90 backdrop-blur-md border-b border-amber-900/40",
        "hero_class": "bg-gradient-to-br from-stone-950 via-neutral-900 to-amber-950",
        "card_class": "bg-stone-900/80 border border-amber-900/30 hover:border-amber-500/60 shadow-2xl rounded-xl",
        "primary_btn_class": "bg-gradient-to-r from-amber-500 to-yellow-600 hover:from-amber-600 hover:to-yellow-700 text-stone-950 font-extrabold shadow-lg shadow-amber-500/20",
        "accent_text_class": "text-amber-400",
        "badge_class": "bg-amber-500/10 text-amber-400 border border-amber-500/30",
        "font_family": "font-serif",
        "hero_layout": "centered",
        "border_radius": "rounded-xl"
    },
    4: {
        "id": 4,
        "name": "Emerald Eco & Bio",
        "description": "Свежая естественная гамма в изумрудно-зеленых оттенках",
        "style_class": "template-emerald",
        "bg_class": "bg-zinc-950 text-zinc-100",
        "header_class": "bg-emerald-950/80 backdrop-blur-md border-b border-emerald-900/50",
        "hero_class": "bg-gradient-to-br from-zinc-950 via-emerald-950 to-teal-950",
        "card_class": "bg-zinc-900/90 border border-emerald-900/40 hover:border-emerald-500/50 shadow-xl rounded-3xl",
        "primary_btn_class": "bg-emerald-500 hover:bg-emerald-600 text-zinc-950 font-bold shadow-lg shadow-emerald-500/25",
        "accent_text_class": "text-emerald-400",
        "badge_class": "bg-emerald-500/10 text-emerald-400 border border-emerald-500/30",
        "font_family": "font-sans",
        "hero_layout": "split-right",
        "border_radius": "rounded-3xl"
    },
    5: {
        "id": 5,
        "name": "Sunset Violet Glam",
        "description": "Яркий закатно-фиолетовый стиль с мягким розоватым градиентом",
        "style_class": "template-sunset",
        "bg_class": "bg-neutral-950 text-neutral-100",
        "header_class": "bg-neutral-900/80 backdrop-blur-md border-b border-fuchsia-900/40",
        "hero_class": "bg-gradient-to-br from-neutral-950 via-fuchsia-950 to-rose-950",
        "card_class": "bg-neutral-900/90 border border-fuchsia-900/30 hover:border-fuchsia-500/50 shadow-xl rounded-2xl",
        "primary_btn_class": "bg-gradient-to-r from-fuchsia-500 to-rose-500 hover:from-fuchsia-600 hover:to-rose-600 text-white font-bold shadow-lg shadow-fuchsia-500/25",
        "accent_text_class": "text-fuchsia-400",
        "badge_class": "bg-fuchsia-500/10 text-fuchsia-400 border border-fuchsia-500/30",
        "font_family": "font-sans",
        "hero_layout": "split-right",
        "border_radius": "rounded-2xl"
    },
    6: {
        "id": 6,
        "name": "Corporate Tech Navy",
        "description": "Строгий деловой темно-синий стиль для корпоративных компаний и инженерии",
        "style_class": "template-navy",
        "bg_class": "bg-slate-900 text-slate-100",
        "header_class": "bg-slate-950/90 backdrop-blur-md border-b border-blue-900/50",
        "hero_class": "bg-gradient-to-br from-slate-950 via-slate-900 to-blue-950",
        "card_class": "bg-slate-800/80 border border-blue-900/40 hover:border-blue-400 shadow-xl rounded-xl",
        "primary_btn_class": "bg-blue-600 hover:bg-blue-500 text-white font-semibold shadow-lg shadow-blue-600/30",
        "accent_text_class": "text-blue-400",
        "badge_class": "bg-blue-500/10 text-blue-300 border border-blue-500/30",
        "font_family": "font-mono",
        "hero_layout": "centered",
        "border_radius": "rounded-xl"
    },
    7: {
        "id": 7,
        "name": "Crimson Fire Sport",
        "description": "Динамичный насыщенный алый стиль для автотехники, спорта и драйва",
        "style_class": "template-crimson",
        "bg_class": "bg-zinc-950 text-zinc-100",
        "header_class": "bg-zinc-900/90 backdrop-blur-md border-b border-red-900/40",
        "hero_class": "bg-gradient-to-br from-zinc-950 via-neutral-900 to-red-950",
        "card_class": "bg-zinc-900/90 border border-red-900/30 hover:border-red-500/60 shadow-xl rounded-lg",
        "primary_btn_class": "bg-red-600 hover:bg-red-700 text-white font-bold shadow-lg shadow-red-600/30",
        "accent_text_class": "text-red-500",
        "badge_class": "bg-red-500/10 text-red-400 border border-red-500/30",
        "font_family": "font-sans",
        "hero_layout": "split-right",
        "border_radius": "rounded-lg"
    },
    8: {
        "id": 8,
        "name": "Cyan Ice Minimal",
        "description": "Прохладный ледяной голубой стиль для медицины, клиник и высоких технологий",
        "style_class": "template-cyan",
        "bg_class": "bg-slate-950 text-slate-100",
        "header_class": "bg-slate-900/80 backdrop-blur-md border-b border-cyan-900/40",
        "hero_class": "bg-gradient-to-br from-slate-950 via-slate-900 to-cyan-950",
        "card_class": "bg-slate-900/90 border border-cyan-900/30 hover:border-cyan-400 shadow-xl rounded-2xl",
        "primary_btn_class": "bg-cyan-500 hover:bg-cyan-600 text-slate-950 font-bold shadow-lg shadow-cyan-500/25",
        "accent_text_class": "text-cyan-400",
        "badge_class": "bg-cyan-500/10 text-cyan-300 border border-cyan-500/30",
        "font_family": "font-sans",
        "hero_layout": "split-right",
        "border_radius": "rounded-2xl"
    },
    9: {
        "id": 9,
        "name": "Warm Amber Construction",
        "description": "Теплый янтарно-оранжевый промышленный стиль для стройки и ремонта",
        "style_class": "template-amber",
        "bg_class": "bg-stone-950 text-stone-100",
        "header_class": "bg-stone-900/90 backdrop-blur-md border-b border-amber-900/40",
        "hero_class": "bg-gradient-to-br from-stone-950 via-stone-900 to-amber-950",
        "card_class": "bg-stone-900/90 border border-amber-900/30 hover:border-amber-500 shadow-xl rounded-2xl",
        "primary_btn_class": "bg-amber-500 hover:bg-amber-600 text-stone-950 font-bold shadow-lg shadow-amber-500/25",
        "accent_text_class": "text-amber-400",
        "badge_class": "bg-amber-500/10 text-amber-400 border border-amber-500/30",
        "font_family": "font-sans",
        "hero_layout": "split-right",
        "border_radius": "rounded-2xl"
    },
    10: {
        "id": 10,
        "name": "Futuristic Glassmorphic",
        "description": "Ультрасовременный стеклянный стиль с эффектом размытия и полупрозрачности",
        "style_class": "template-glass",
        "bg_class": "bg-gray-950 text-gray-100",
        "header_class": "bg-white/10 backdrop-blur-lg border-b border-white/10 shadow-2xl",
        "hero_class": "bg-gradient-to-tr from-indigo-950 via-slate-900 to-teal-950",
        "card_class": "bg-white/5 backdrop-blur-md border border-white/10 hover:border-white/20 shadow-2xl rounded-3xl",
        "primary_btn_class": "bg-gradient-to-r from-teal-400 to-indigo-500 hover:from-teal-500 hover:to-indigo-600 text-slate-950 font-extrabold shadow-lg shadow-teal-500/20",
        "accent_text_class": "text-teal-300",
        "badge_class": "bg-white/10 text-teal-300 border border-white/20 backdrop-blur-md",
        "font_family": "font-sans",
        "hero_layout": "centered",
        "border_radius": "rounded-3xl"
    }
}

CATEGORY_CONFIGS = {
    "auto": {
        "badge": "Автосервис & Детейлинг",
        "hero_title": "Профессиональный ремонт и обслуживание вашего авто",
        "hero_subtitle": "Гарантия на все работы, современные диагносты и качественные запчасти в наличии.",
        "primary_color": "amber",
        "default_template_id": 7,
        "features": [
            {"title": "Компьютерная диагностика", "desc": "Точное выявление неисправностей на дилерском оборудовании", "icon": "fa-microchip"},
            {"title": "Ремонт ДВС и КПП", "desc": "Капитальный ремонт агрегатов любой сложности с гарантией", "icon": "fa-gears"},
            {"title": "Техническое обслуживание", "desc": "Замена масла, фильтров, жидкостей и колодок за 45 минут", "icon": "fa-wrench"},
            {"title": "Детейлинг и полировка", "desc": "Защитные покрытия керамикой и идеальный блеск кузова", "icon": "fa-car-side"}
        ],
        "services": [
            {"name": "Диагностика подвески и тормозов", "price": "от 800 ₽"},
            {"name": "Плановое ТО (замена масла + фильтры)", "price": "от 1 500 ₽"},
            {"name": "Сход-развал 3D", "price": "от 1 800 ₽"},
            {"name": "Ремонт тормозной системы", "price": "от 2 000 ₽"},
            {"name": "Заправка и обслуживание автокондиционера", "price": "от 2 500 ₽"}
        ],
        "advantages": [
            "Гарантия 12 месяцев на все выполненные работы",
            "Собственный склад оригинальных запчастей и аналогов",
            "Комфортная зона ожидания с кофейней, Wi-Fi и ТВ",
            "Прозрачная сметная стоимость до начала ремонта"
        ],
        "banner_img": "https://images.unsplash.com/photo-1486006920555-c77dce18193b?auto=format&fit=crop&w=1200&q=80"
    },
    "construction": {
        "badge": "Строительство & Ремонт",
        "hero_title": "Строительство домов и комплексный ремонт помещений",
        "hero_subtitle": "Строго по Договору, с фиксированной сметой и соблюдением всех СНиП и ГОСТ.",
        "primary_color": "blue",
        "default_template_id": 9,
        "features": [
            {"title": "Строительство «Под ключ»", "desc": "От возведения фундамента до финишной отделки и интерьера", "icon": "fa-house-chimney"},
            {"title": "Дизайн-проекты", "desc": "3D-визуализация, планировки и подбор отделочных материалов", "icon": "fa-compass-drafting"},
            {"title": "Капитальный ремонт", "desc": "Полный комплекс инженерных и отделочных работ в срок", "icon": "fa-hammer"},
            {"title": "Технический надзор", "desc": "Контроль качества каждого этапа инженером-технологом", "icon": "fa-clipboard-check"}
        ],
        "services": [
            {"name": "Проектирование и 3D визуализация", "price": "от 600 ₽/м²"},
            {"name": "Черновая отделка и электромонтаж", "price": "от 3 500 ₽/м²"},
            {"name": "Капитальный ремонт квартир и офисов", "price": "от 7 000 ₽/м²"},
            {"name": "Строительство загородного дома", "price": "от 35 000 ₽/м²"}
        ],
        "advantages": [
            "Фиксированная сметка — цена не изменится в процессе",
            "Оплата поэтапно по факту принятых работ",
            "Скидки до 20% на стройматериалы от партнеров",
            "Видеонаблюдение на объекте 24/7 для заказчика"
        ],
        "banner_img": "https://images.unsplash.com/photo-1503387762-592deb58ef4e?auto=format&fit=crop&w=1200&q=80"
    },
    "store": {
        "badge": "Магазин & Торговля",
        "hero_title": "Широкий ассортимент качественных товаров по лучшим ценам",
        "hero_subtitle": "Быстрая доставка, официальная гарантия и программа лояльности для покупателей.",
        "primary_color": "emerald",
        "default_template_id": 4,
        "features": [
            {"title": "Оригинальная продукция", "desc": "Прямые поставки от проверенных производителей и брендов", "icon": "fa-certificate"},
            {"title": "Быстрая доставка", "desc": "Отправка в день заказа курьером или в пункты выдачи", "icon": "fa-truck-fast"},
            {"title": "Гарантия возврата", "desc": "Удобный обмен и возврат товара в течение 14 дней", "icon": "fa-rotate-left"},
            {"title": "Бонусная программа", "desc": "Кешбэк с каждой покупки и скидки постоянным клиентам", "icon": "fa-gift"}
        ],
        "services": [
            {"name": "Курьерская доставка по городу", "price": "Бесплатно от 3 000 ₽"},
            {"name": "Самовывоз из магазина", "price": "0 ₽ (сегодня)"},
            {"name": "Подарочная упаковка", "price": "от 250 ₽"},
            {"name": "Консультация эксперта", "price": "Бесплатно"}
        ],
        "advantages": [
            "Более 5 000 наименований всегда в наличии",
            "Удобные способы оплаты: картой, SberPay, СБП",
            "Регулярные распродажи и специальные акции",
            "Сертифицированные и экологичные товары"
        ],
        "banner_img": "https://images.unsplash.com/photo-1441986300917-64674bd600d8?auto=format&fit=crop&w=1200&q=80"
    },
    "beauty": {
        "badge": "Салон Красоты & Esthetic",
        "hero_title": "Ваша безупречная красота и стиль в руках профессионалов",
        "hero_subtitle": "Первоклассные мастера, премиальная косметика и атмосфера полного релакса.",
        "primary_color": "rose",
        "default_template_id": 5,
        "features": [
            {"title": "Стилисты & Парикмахеры", "desc": "Стрижки, сложное окрашивание, уходовые процедуры для волос", "icon": "fa-scissors"},
            {"title": "Nail-сервис", "desc": "Аппаратный маникюр, педикюр и авторский дизайн ногтей", "icon": "fa-hand-sparkles"},
            {"title": "Косметология", "desc": "Чистки, пилинги, уход за кожей и омолаживающие программы", "icon": "fa-sparkles"},
            {"title": "Визаж & Брови", "desc": "Архитектура бровей, ламинирование ресниц, вечерний макияж", "icon": "fa-eye"}
        ],
        "services": [
            {"name": "Женская стрижка + укладка", "price": "от 1 800 ₽"},
            {"name": "Маникюр с покрытием Gel-LAK", "price": "от 1 900 ₽"},
            {"name": "Сложное окрашивание (Airtouch, Balayage)", "price": "от 4 500 ₽"},
            {"name": "Уходовая процедура для лица", "price": "от 2 500 ₽"}
        ],
        "advantages": [
            "100% стерильность инструментов и одноразовые расходники",
            "Использование премиальной косметики (L'Oreal, Kerastase, Luxio)",
            "Вкусный кофе, Prosecco и уютная атмосфера для каждого гостя",
            "Удобная онлайн-запись в любое время 24/7"
        ],
        "banner_img": "https://images.unsplash.com/photo-1560066984-138dadb4c035?auto=format&fit=crop&w=1200&q=80"
    },
    "medical": {
        "badge": "Медицинский Центр & Здоровье",
        "hero_title": "Забота о вашем здоровье с заботой и вниманием",
        "hero_subtitle": "Опытные врачи высшей категории, современная диагностика и бережный подход.",
        "primary_color": "cyan",
        "default_template_id": 8,
        "features": [
            {"title": "Прием специалистов", "desc": "Терапевты, узкие специалисты и врачи высшей категории", "icon": "fa-user-doctor"},
            {"title": "Лабораторная диагностика", "desc": "Более 1000 видов анализов с быстрой выдачей результатов", "icon": "fa-vial-virus"},
            {"title": "УЗИ и Функциональная диагностика", "desc": "УЗИ всех органов на аппарате экспертного класса", "icon": "fa-heart-pulse"},
            {"title": "Стоматология", "desc": "Лечение без боли, имплантация, эстетическая стоматология", "icon": "fa-tooth"}
        ],
        "services": [
            {"name": "Первичный прием врача-специалиста", "price": "от 1 800 ₽"},
            {"name": "Комплексное УЗИ исследование", "price": "от 2 200 ₽"},
            {"name": "Профессиональная гигиена полости рта", "price": "от 3 500 ₽"},
            {"name": "Чекап организма (Базовый)", "price": "от 6 900 ₽"}
        ],
        "advantages": [
            "Врачи с многолетним практическим опытом и учеными степенями",
            "Отсутствие очередей и прием строго по предварительной записи",
            "Современное медицинское оборудование стандартов ЕС",
            "Полная конфиденциальность и электронная медицинская карта"
        ],
        "banner_img": "https://images.unsplash.com/photo-1629909613654-28e377c37b09?auto=format&fit=crop&w=1200&q=80"
    },
    "general": {
        "badge": "Услуги & Бизнес",
        "hero_title": "Надежные решения и профессиональные услуги для вас",
        "hero_subtitle": "Высокое качество, индивидуальный подход и строгое соблюдение сроков.",
        "primary_color": "indigo",
        "default_template_id": 1,
        "features": [
            {"title": "Высокое качество", "desc": "Многоступенчатый контроль качества выполнения каждой задачи", "icon": "fa-award"},
            {"title": "Индивидуальный подход", "desc": "Подбираем оптимальные решения под ваши требования и бюджет", "icon": "fa-handshake"},
            {"title": "Оперативность", "desc": "Быстрое выполнение заказов без потери качества", "icon": "fa-clock"},
            {"title": "Гарантия результата", "desc": "Официальный договор и несем ответственность за результат", "icon": "fa-shield-halved"}
        ],
        "services": [
            {"name": "Консультация специалиста", "price": "Бесплатно"},
            {"name": "Базовый пакет услуг", "price": "от 3 000 ₽"},
            {"name": "Комплексное обслуживание", "price": "от 10 000 ₽"},
            {"name": "Индивидуальный проект", "price": "По запросу"}
        ],
        "advantages": [
            "Опыт работы на рынке и отличная репутация",
            "Гибкая система скидок для постоянных клиентов",
            "Всегда на связи и готовы проконсультировать",
            "Удобное расположение и комфортное обслуживание"
        ],
        "banner_img": "https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=1200&q=80"
    }
}

def get_category_config(category_key: str) -> dict:
    return CATEGORY_CONFIGS.get(category_key, CATEGORY_CONFIGS["general"])

def get_template_config(template_id: int) -> dict:
    return TEMPLATES_CONFIG.get(template_id, TEMPLATES_CONFIG[1])
