.PHONY: remote
remote:
	@docker run -d -p 4444:4444 -v /dev/shm:/dev/shm selenium/standalone-chrome-debug
