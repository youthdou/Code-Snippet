#ifndef QTSNIPPET_H
#define QTSNIPPET_H

#include <QDebug>

#define     TRACE(strMsg)           qDebug() << "[" << __FUNCTION__ << "]" << strMsg

#endif // QTSNIPPET_H
