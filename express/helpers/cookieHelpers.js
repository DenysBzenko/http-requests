function setCookie(res, cookieName, cookieValue, httpOnly) {
    const options = {
      httpOnly: httpOnly,
    };
    res.cookie(cookieName, cookieValue, options);
  }
  
  function getCookie(req, cookieName) {
    const cookieValue = req.cookies ? req.cookies[cookieName] : null;
    return cookieValue || 'Cookie not found';
  }
  
  module.exports = { setCookie, getCookie };
  