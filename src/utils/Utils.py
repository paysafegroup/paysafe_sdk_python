'''
Created on 24-May-2016

@author: asawari.vaidya
'''
import json


class Utils(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        
        
    def _generate_error(response_error):
        response = "{"
        for keys, values in response_error.__dict__.items():
            if isinstance(values, list):
                response += "\""
                response += keys
                response += "\":["
                for count in range(values.__len__()):
                    if isinstance(values[count], dict):
                        response += json.dumps(values[count].__dict__)
                    elif isinstance(values[count], str):
                        response += json.dumps(values[count])    
                    response += ","
                response = response[:-1]
                response += "],"
            else:
                response += "\""
                response += keys
                response += "\":\""
                if isinstance(values, int):
                    response += str(values)
                else:
                    response += values
                response += "\","
        response = response[:-1]
        response += "}"
        
        return (response)
    
            
    @classmethod
    def print_response(self, response_object):
        response = "{"
        for keys,values in response_object.__dict__.items():
            if isinstance(values, dict):
                if keys == "error":
                    response += "\""
                    response += keys
                    response += "\":"
                    response += self._generate_error(values)
                    response += ","
                else:
                    response += "\""
                    response += keys
                    response += "\":"
                    if values.__dict__.__len__() > 1:
                        response += "{"
                        for keys1, values1 in values.__dict__.items():
                            response += "\""
                            response += keys1
                            response += "\":"
                            if isinstance(values1, dict):
                                response += json.dumps(values1.__dict__)
                                response += ","
                            else:
                                response += json.dumps(values1)
                                response += ","
                        response = response[:-1]           
                        response += "},"
                    else:    
                        response += json.dumps(values.__dict__)
                    response += ","
                    response = response[:-1]        
            elif isinstance(values, list):
                response += "\""
                response += keys
                response += "\":["
                for count in range(values.__len__()):
                    response += "{"
                    for keys,values11 in values[count].__dict__.items():
                        if isinstance(values11, dict):
                            response += "\""
                            response += keys
                            response += "\":"
                            if values11.__dict__.__len__() > 1:
                                response += "{"
                                for keys1, values1 in values11.__dict__.items():
                                    response += "\""
                                    response += keys1
                                    response += "\":"
                                    if isinstance(values1, dict):
                                        response += json.dumps(values1.__dict__)
                                    else:
                                        response += json.dumps(values1)
                                    response += ","
                                response = response[:-1]
                                response += "}"
                            else:
                                response += json.dumps(values11.__dict__)
                            response += ","
                        elif isinstance(values11, list):
                            response += "\""
                            response += keys
                            response += "\":["
                            for count in range(values11.__len__()):
                                response += json.dumps(values11[count].__dict__)
                                response += ","
                            response = response[:-1]
                            response += "],"
                        else:
                            response += "\""
                            response += keys
                            response += "\":\""
                            response += str(values11)
                            response += "\","    
                    response = response[:-1]
                    response += "},"
                response = response[:-1]    
                response += "],"
            else:
                response += "\""
                response += keys
                response += "\":\""
                if values is None:
                    response += "None"
                else:
                    if isinstance(values, int):
                        response += str(values)
                    else:
                        response += str(values)
                response += "\","
        response = response[:-1]
        response += "}"
        
        # Print Response
        print (response)