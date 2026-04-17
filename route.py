from flask import Flask, render_template, request

app= Flask(__name__)

@app.route('/')
def menu():
    return render_template('menu.html')

@app.route('/explore')
def explore():
    product_id= request.args.get('product_id', type=int)
    products = {
        1: {"id": "1","name": "iPhone 17", "price": "$999", "image": "iphone17.png",  
            "description1": "Brighter display, now with ProMotion up to 120Hz. Durable Ceramic Shield 2 front with 3x better scratch resistance.","image1": "iphone17s1.png",
            "description2": "48MP Dual Fusion camera system. Superstunning shots up close and far away.","image2": "iphone17s2.png",
            "description3": "Apple Intelligence. Effortlessly helpful features — from image creation to Live Translation.3","image3": "iphone17s3.png",
            "camera":"48MP Dual Fusion camera system", 
           "chip":"A19 chip6‑core CPU with 2 performance and 4 efficiency cores 5‑core GPU with Neural Accelerators 16‑core Neural Engine Hardware-accelerated ray tracing", 
           "video":"4K Dolby Vision video recording at 24 fps, 25 fps, 30 fps, or 60 fps",
           "frontCam":"18MP Center Stage camera",
           "powerBattery": "Up to 30 hours",
           "memory": "256GB 8GB RAM, 512GB 8GB RAM",
           "weight":"177g",
           "height":"149.6mm",
           "depth":"7.95mm",
           "width":"71.5mm",

            
            
            }
        ,
        2: {"id": "2","name": "iPhone 17 Air", "price": "$1299", "image": "iphone17Airs.png", 
            
            "description1": "Super thin. Strikingly light. Shockingly strong.","image1": "iphone17Airs1.png",
            "description2": "A19 Pro chip and all‑day battery life.1 Pro within thin.","image2": "iphone17Airs2.png",
            "description3": "iOS 26. New look. Even more magic.","image3": "iphone17Airs3.png",
             "camera":"48MP Dual Fusion camera system", 
           "chip":"A19 chip6‑core CPU with 2 performance and 4 efficiency cores 5‑core GPU with Neural Accelerators 16‑core Neural Engine Hardware-accelerated ray tracing", 
           "video":"4K Dolby Vision video recording at 24 fps, 25 fps, 30 fps, or 60 fps",
           "frontCam":"18MP Center Stage camera",
           "powerBattery": "Up to 30 hours",
           "memory": "256GB 8GB RAM, 512GB 8GB RAM",
           "weight":"165g",
           "height":"156.22mm",
           "depth":"5.64",
           "width":"74.7mm",
            
            },
        3: {"id": "3","name": "iPhone 17 Pro", "price": "$1499", "image": "iphone17Pro.png",
            
            "description1": "iOS 26. New look. Even more magic.","image1": "iphone17Pros1.png",
            "description2": "A19 Pro, vapor cooled for lightning‑fast performance. Breakthrough battery life.","image2": "iphone17Pros2.png",
            "description3": "Heat‑forged aluminum unibody design for exceptional pro capability.","image3": "iphone17Pros3.png",
            "camera":"48MP Pro Fusion camera system", 
           "chip":"A19 Pro chip 6‑core CPU with 2 performance and 4 efficiency cores 6‑core GPU with Neural Accelerators 16‑core Neural Engine Hardware‑accelerated ray tracing", 
           "video":"4K Dolby Vision video recording at 24 fps, 25 fps, 30 fps, 60 fps, 100 fps (Fusion Main), or 120 fps (Fusion Main)",
           "frontCam":"18MP Center Stage camera",
           "powerBattery": "Up to 37 hours",
           "memory": "256GB 12GB RAM, 512GB 12GB RAM, 1TB 12GB RAM",
           "weight":"204g",
           "height":"150.0mm",
           "depth":"8.75",
           "width":"71.9mm",
            
             
             },
    }   


    product= products.get(product_id, products[1])


    return render_template('explore.html', product=product)


@app.route('/box')
def box():
    product_id= request.args.get('product_id', type=int)

    products={
        1:{"name": "iPhone 17 ",
           "item1":"iPhone with iOS 26", "item2":"USB‑C Charge Cable (1m)", "item3":"Documentation",
           "image": "iphone17Box"
           
           
           
           },
        2:{"name": "iPhone 17 Air",
           "item1":"iPhone with iOS 26", "item2":"USB‑C Charge Cable (1m)", "item3":"Documentation",
           "image": "iphone17AirBox"
           
           },


        3:{"name": "iPhone 17 Pro",
           "item1":"iPhone with iOS 26", "item2":"USB‑C Charge Cable (1m)", "item3":"Documentation",
           "image": "iphone17ProBox"},
    }

    product=products.get(product_id, products[1])

    return render_template('box.html', product=product)



@app.route('/buy')
def buy():
    product_id=request.args.get('product_id', type=int)

    products={
        1:{"name": "iPhone 17 ", 
           "color1": "Black", "color2": "White",  "color3": "Mist  Blue", "color4": "Sage", "color5": "Lavender", 
           "storage1": "256GB", "storage2": "512GB",
           "colorImages": "iphone17Colors.png", 
           
           
           
           
           },
        2:{"name": "iPhone 17 Air",
           "color1": "Space Black", "color2": "Cloud White",  "color3": "Light Gold", "color4": "Sky Blue", 
           "storage1": "256GB", "storage2": "512GB",  "storage3": "1TB",
           "colorImages": "iphone17AirColors.png", 
           
           
           
           
           },





        3:{"name": "iPhone 17 Pro",
           "color1": "Silver", "color2": "Cosmic Orange",  "color3": "Deep Blue", 
           "storage1": "256GB", "storage2": "512GB",  "storage3": "1TB", "storage4": "2TB", 
           "colorImages": "iphone17ProColors.png", 
           
   
           },
    }

    product=products.get(product_id, products[1])
    return render_template('buy.html', product=product)





@app.route('/features')
def features():





    feature={
            "feature1": "gaming",
            "gamingImg": "img/features/benchmark.png",
              "gamingInfo" : "The A19 on the iPhone 17 is set to offer about 20 percent faster GPU performance when compared with the A18, and about 80 percent faster when compared with the A16 Bionic from the iPhone 15. Compared with the iPhone 13 with A15 Bionic launched in 2021, the latest base iPhone will offer twice the GPU performance.",
         
            "feature2": "Operating System",
              "OSImg": "img/features/OS.png",
              "OSInfo" : "The release delivers a stunning new design, powerful Apple Intelligence capabilities, new ways to stay connected in the Phone and Messages apps, and exciting updates to CarPlay, Apple Music, Maps, and Wallet",

              "feature3": "Security",
              "SecurityImg": "img/features/security.png",
              "SecurityInfo" : "Apple has added a groundbreaking new memory security feature to its new iPhone 17 lineup called Memory Integrity Enforcement (MIE), which the company describes as the most significant upgrade to memory safety in the history of consumer operating systems.",



    }



    return render_template('features.html', feature=feature)





@app.route('/useCase')
def useCase():
    
    feature={
            "feature1": "Video",
            "VideoImg": "img/realcase/vid.png",
              "VideoInfo" : " Genlock and time code support. Allows superprecise video synchronization, which is useful for content creators and Hollywood productions alike. Supported via the new Blackmagic Camera ProDock.",
         
            "feature2": "Photo",
              "PhotoImg": "img/realcase/photo.png",
              "PhotoInfo" : " Low-light photography and Night mode. Capture sharp, detailed, bright images with natural colors, even when it’s dark. ",

              "feature3": "Gaming",
              "GamingImg": "img/realcase/gaming.jpg",
              "GamingInfo" : "With Neural Accelerators integrated into each GPU core, iPhone 17 Pro is more powerful than ever when working with local AI models.",

              "feature4": "MultiTask",
              "MultiTaskImg": "img/realcase/multitask.png",
              "MultiTaskInfo" : "With Picture in Picture, you can watch a video or use FaceTime while you use other apps.",

            "feature5": "Productivity",
              "ProductivityImg": "img/realcase/productivity.png",
              "ProductivityInfo" : "Siri draws on Apple Intelligence for new superpowers. With an all-new design, richer language understanding, and the ability to type to Siri whenever it’s convenient for you, communicating with Siri is more natural than ever. And with extensive product knowledge and the ability to tap into ChatGPT when it might be helpful to answer your question, Siri can assist you in brand-new ways.",

               "feature6": "Communication",
              "CommunicationImg": "img/realcase/esim.png",
              "CommunicationInfo" : "An eSIM is an industry-standard digital SIM built into your iPhone, eliminating the need for a physical SIM card. This innovative feature enables you to switch between SIMs effortlessly, manage up to eight or more eSIMs, and activate new plans digitally. With eSIM, you enjoy greater flexibility, enhanced convenience, better security, and seamless connectivity, especially when traveling internationally.",

    }
    return render_template('useCase.html', feature=feature)




@app.route('/specs')
def specs():
    product_id= request.args.get('prodcut_id', type=int)

    products={
        1:{"name": "iPhone 17 ",
           "camera":"48MP Dual Fusion camera system", 
           "chip":"A19 chip6‑core CPU with 2 performance and 4 efficiency cores 5‑core GPU with Neural Accelerators 16‑core Neural Engine Hardware-accelerated ray tracing", 
           "video":"4K Dolby Vision video recording at 24 fps, 25 fps, 30 fps, or 60 fps",
           "frontCam":"18MP Center Stage camera",
           "powerBattery": "Up to 30 hours",
           "memory": "256GB 8GB RAM, 512GB 8GB RAM",
           "weight":"177g",
           "height":"149.6mm",
           "depth":"7.95mm",
           "width":"71.5mm",
           
           
           
           },
        2:{"name": "iPhone 17 Air",
           "camera":"48MP Dual Fusion camera system", 
           "chip":"A19 chip6‑core CPU with 2 performance and 4 efficiency cores 5‑core GPU with Neural Accelerators 16‑core Neural Engine Hardware-accelerated ray tracing", 
           "video":"4K Dolby Vision video recording at 24 fps, 25 fps, 30 fps, or 60 fps",
           "frontCam":"18MP Center Stage camera",
           "powerBattery": "Up to 30 hours",
           "memory": "256GB 8GB RAM, 512GB 8GB RAM",
           "weight":"165g",
           "height":"156.22mm",
           "depth":"5.64",
           "width":"74.7mm",
           
           },


        3:{"name": "iPhone 17 Pro",
           "camera":"48MP Pro Fusion camera system", 
           "chip":"A19 Pro chip 6‑core CPU with 2 performance and 4 efficiency cores 6‑core GPU with Neural Accelerators 16‑core Neural Engine Hardware‑accelerated ray tracing", 
           "video":"4K Dolby Vision video recording at 24 fps, 25 fps, 30 fps, 60 fps, 100 fps (Fusion Main), or 120 fps (Fusion Main)",
           "frontCam":"18MP Center Stage camera",
           "powerBattery": "Up to 37 hours",
           "memory": "256GB 12GB RAM, 512GB 12GB RAM, 1TB 12GB RAM",
           "weight":"204g",
           "height":"150.0mm",
           "depth":"8.75",
           "width":"71.9mm",
           
           },
    }

    return render_template('specs.html')



if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
