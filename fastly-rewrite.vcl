if (req.url !~ "^/margin-framer-template") {
  set req.url = "/margin-framer-template" + req.url;
}
