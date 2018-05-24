import logging                                                                  
import logging.handlers  
from flask import Flask                                                      
                                                                                  
app = Flask(__name__)     

# Add RotatingFileHandler to Flask Logger
handler = logging.handlers.RotatingFileHandler("test.log", "a+", maxBytes=3000, backupCount=5)
handler.setLevel(logging.INFO) 
handler.setFormatter(logging.Formatter('[%(asctime)s] %(levelname)s in %(module)s: %(message)s'))
app.logger.addHandler(handler)

@app.route('/')                                                                 
def index():                                                                    
    app.logger.debug('debug')                                                   
    app.logger.info('info')                                                     
    app.logger.warn('warn')                                                     
    app.logger.error('error')                                                   
    app.logger.critical('critical')                                                                                                                         
    return "logging"                                                            
                                                                                                                                                    
if __name__ == '__main__':                                                      
    app.run(debug=True)     
