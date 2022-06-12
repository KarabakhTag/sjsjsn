
### 🚀 Deploy to heroku
[![Deploy]({

  "name": "Tesla Game V1 Versiyon",

  "description": " @QafqazTeslaBot'un Eski Alt Versiyon Projesi GitHub'da Kullanıcılara Açık Sunuldu.",

  "repository": "https://github.com/sirincay/TeslaGamev1",

  "logo": "https://avatars.githubusercontent.com/u/88708263?s=96&v=4",

  "keywords": ["telegram", "bot"],

  "env": {

    "TOKEN": {

      "description": "@BotFather'dan oluşturduğunuz botun tokeni.",

      "value": ""

    },

    "ID_BOT": {

      "description": "Botun ID Yazın (İlk Rakamlar)",

      "value": ""

    },

    "BOT_ISMI": {

      "description": "Botun Kullanıcı Adını '@' Olmadan Yazın",

      "value": "QafqazTeslaBot"

    },

    "RAUND_SAYI": {

      "description": "RAUND SAYISI (3-5) İdeal aralık ",

      "value": "3"

    },

    "SANIYE": {

      "description": "Resimlerin Değişmesi Süresi / 10000=10 Saniye",

      "value": "10000"

      }

  },

  "buildpacks": [

    {

      "url": "heroku/nodejs"

    }

  ],

  "formation": {

    "worker": {

      "quantity": 1

    }

  }

}
