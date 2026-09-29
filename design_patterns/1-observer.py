#!/usr/bin/env python3
"""
Observer Pattern - News Subject Notification System
"""
from abc import ABC, abstractmethod
from typing import Dict, Optional, Set


class Observer(ABC):
    """Abstract observer class."""
    @abstractmethod
    def update(self, topic: str, data: str) -> None:
        """Receive update notification from subject."""
        pass


class Subject:
    """Core subject handling observer registration and notification."""
    def __init__(self) -> None:
        self._observers: Dict[Observer, Optional[Set[str]]] = {}

    def subscribe(self, observer: Observer, topics: Optional[Set[str]] = None) -> None:
        self._observers[observer] = topics

    def unsubscribe(self, observer: Observer) -> None:
        self._observers.pop(observer, None)

    def notify(self, topic: str, data: str) -> None:
        for observer, topics in list(self._observers.items()):
            if topics is None or topic in topics:
                observer.update(topic, data)


class NewsSubject:
    """News publisher using internal Subject."""
    def __init__(self) -> None:
        self._subject = Subject()

    def subscribe(self, observer: Observer, topics: Optional[Set[str]] = None) -> None:
        self._subject.subscribe(observer, topics)

    def unsubscribe(self, observer: Observer) -> None:
        self._subject.unsubscribe(observer)

    def publish(self, topic: str, data: str) -> None:
        self._subject.notify(topic, data)


class LogObserver(Observer):
    """Observer that logs updates."""
    def update(self, topic: str, data: str) -> None:
        print(f"log:{topic}={data}")


class EmailObserver(Observer):
    """Observer that emails updates."""
    def update(self, topic: str, data: str) -> None:
        print(f"email:{topic}={data}")


class SmsObserver(Observer):
    """Observer that sends SMS updates."""
    def update(self, topic: str, data: str) -> None:
        print(f"sms:{topic}={data}")


def main() -> None:
    """Main execution function."""
    news = NewsSubject()

    log_observer = LogObserver()
    email_observer = EmailObserver()
    sms_observer = SmsObserver()

    news.subscribe(log_observer, topics={"sports", "breaking"})
    news.subscribe(email_observer)
    news.subscribe(sms_observer, topics={"breaking"})

    news.publish("weather", "rain")
    news.publish("sports", "goal")
    news.publish("breaking", "alert")


if __name__ == "__main__":
    main()
