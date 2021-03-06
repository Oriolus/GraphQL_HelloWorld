GO
/****** Object:  Table [azs]    Script Date: 3/10/2019 11:02:21 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [azs](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[address] [nvarchar](1024) NULL,
	[number] [nchar](512) NULL,
	[departmentId] [int] NULL,
	[lat] [float] NULL,
	[lon] [float] NULL,
	[goldRecordId] [int] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [department]    Script Date: 3/10/2019 11:02:21 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [department](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[title] [nvarchar](256) NOT NULL
) ON [PRIMARY]
GO
/****** Object:  Table [kkt]    Script Date: 3/10/2019 11:02:21 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [kkt](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[inn] [nvarchar](128) NULL,
	[kktRegId] [nvarchar](128) NULL,
	[driveFistNumber] [nvarchar](128) NOT NULL,
	[loadingCode] [int] NOT NULL
) ON [PRIMARY]
GO
