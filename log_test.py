from flask import Flask                                                         
                                                                                  
app = Flask(__name__)                                                                                                                          
                                                                            
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
